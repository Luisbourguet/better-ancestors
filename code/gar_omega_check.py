"""Recompute the worked example of "Better Ancestors: What Constitutions Owe the
Unborn" (Section 5: the orders Omega, Omega* and Omega') from Definitions 1-6
and conventions K2-K5 of the article, plus two sensitivity orders.

RULE_I = 'either' is the definition stated in the article: condition (i) holds
when a norm lies within the scope of an accessible procedure of either kind
(formal amendment or authoritative interpretation). 'amendment_only' is a
stricter variant, printed for comparison only.

Run:  python3 code/gar_omega_check.py
Expected (rule 'either'): V(Omega) = 2/3, V(Omega*) = 0, V(Omega') = 1/3.
"""
from math import inf

RULE_I = 'either'            # the article's definition; 'amendment_only' = stricter variant

# ---------- Definition 3: access (seat-level, majority rule D17) ----------

def accessible(body, bodies):
    if body == 'electorate':
        return True
    seats = bodies[body]['seats']
    settled = 0
    for s in seats:
        if s['vacancy'] != 'term':
            continue
        f = s['filled_by']
        if f == 'electorate' or (f in bodies and accessible(f, bodies)):
            settled += 1
    return settled > len(seats) / 2

# ---------- Definition 4: cost ----------

def cost(proc):
    s = len(proc['stages'])
    q = 1 if any(st['qualified'] for st in proc['stages']) else 0
    return s + q

def kind_of(proc, bodies):
    acc = [accessible(st['body'], bodies) for st in proc['stages']]
    if all(acc):
        return 'accessible'
    if not any(acc):
        return 'alien'
    return 'mixed'  # enters no cost (Definition 3, last clause)

# ---------- Definitions 5-6 ----------

def evaluate(order, rule_i=None):
    rule_i = rule_i or RULE_I
    bodies, N, procs = order['bodies'], order['N'], order['P']
    N_T = list(N)                                   # K2
    amend_cost, interp_acc, c_x = {}, {}, {}
    for n in N_T:
        a = ia = cx = inf
        for p in procs:
            if n not in p['scope']:
                continue
            k, c = kind_of(p, bodies), cost(p)
            if k == 'accessible':
                if p['kind'] == 'amendment':
                    a = min(a, c)
                else:
                    ia = min(ia, c)
            elif k == 'alien':
                cx = min(cx, c)
        amend_cost[n], interp_acc[n], c_x[n] = a, ia, cx
    for m, n in order.get('protects', []):           # K3, amendment routes
        amend_cost[m] = max(amend_cost[m], amend_cost[n])
        if amend_cost[n] == inf:
            amend_cost[m] = inf
    c_G = {n: min(amend_cost[n], interp_acc[n]) for n in N_T}
    rows, fails = [], 0
    for n in N_T:
        fail_i = (amend_cost[n] == inf) if rule_i == 'amendment_only' else (c_G[n] == inf)
        fail_ii = c_G[n] > c_x[n]
        fails += (fail_i or fail_ii)
        rows.append((n, amend_cost[n], c_G[n], c_x[n], fail_i, fail_ii))
    return rows, fails / len(N_T)

# ---------- Bodies and procedures ----------

legislature = {'seats': [{'vacancy': 'term', 'filled_by': 'electorate'}] * 5}
council     = {'seats': [{'vacancy': 'life', 'filled_by': 'self'}] * 5}
court       = {'seats': [{'vacancy': 'term', 'filled_by': 'Legislature'}] * 5}   # elected-by-Legislature, fixed terms

amend_2_3     = {'kind': 'amendment', 'scope': {'Art.2', 'Art.3'},
                 'stages': [{'body': 'Legislature', 'qualified': True}]}
amend_art1    = {'kind': 'amendment', 'scope': {'Art.1'},
                 'stages': [{'body': 'Legislature', 'qualified': True},
                            {'body': 'electorate', 'qualified': False}]}
council_int_1 = {'kind': 'interpretation', 'scope': {'Art.1'},
                 'stages': [{'body': 'Council', 'qualified': False}]}
court_int_all = {'kind': 'interpretation', 'scope': {'Art.1', 'Art.2', 'Art.3'},
                 'stages': [{'body': 'Court', 'qualified': False}]}

Omega      = {'N': ['Art.1', 'Art.2', 'Art.3'], 'bodies': {'Legislature': legislature},
              'P': [amend_2_3], 'protects': [('Art.3', 'Art.1')]}
OmegaStar  = {'N': ['Art.1', 'Art.2', 'Art.3'], 'bodies': {'Legislature': legislature},
              'P': [amend_2_3, amend_art1], 'protects': [('Art.3', 'Art.1')]}
OmegaPrime = {'N': ['Art.1', 'Art.2', 'Art.3'], 'bodies': {'Legislature': legislature, 'Council': council},
              'P': [amend_2_3, amend_art1, council_int_1], 'protects': [('Art.3', 'Art.1')]}
# Sensitivity: Omega's eternity clause under an accessible court with final interpretive authority
OmegaCourt = {'N': ['Art.1', 'Art.2', 'Art.3'], 'bodies': {'Legislature': legislature, 'Court': court},
              'P': [amend_2_3, court_int_all], 'protects': [('Art.3', 'Art.1')]}
# Sensitivity: Omega's eternity clause guarded by the life-tenured Council
OmegaGuard = {'N': ['Art.1', 'Art.2', 'Art.3'], 'bodies': {'Legislature': legislature, 'Council': council},
              'P': [amend_2_3, council_int_1], 'protects': [('Art.3', 'Art.1')]}

if __name__ == '__main__':
    cases = [('Omega', Omega), ('Omega*', OmegaStar), ("Omega'", OmegaPrime),
             ('Omega + accessible court (sensitivity)', OmegaCourt),
             ('Omega + Council guarding Art.1 (sensitivity)', OmegaGuard)]
    for rule in ('amendment_only', 'either'):
        print(f"\n===== condition (i) rule: {rule} =====")
        for name, order in cases:
            rows, V = evaluate(order, rule)
            print(f"{name}:  V = {V:.4f}")
            for n, a, cg, cx, fi, fii in rows:
                print(f"   {n}: amend={a} c_G={cg} c^x_G={cx} fails(i)={fi} fails(ii)={fii}")
