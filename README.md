# Better Ancestors: What Constitutions Owe the Unborn

**Luis Bourguet** — LabOnt – Center for Ontology, Università degli Studi di Torino; Complex Systems Science Laboratory, Hiroshima University. ORCID [0000-0002-4673-4486](https://orcid.org/0000-0002-4673-4486).

Preprint, version 1 (22 October 2026). Under double-anonymous peer review at a journal (venue withheld until decision); not yet peer reviewed. Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Archived version:** DOI assigned by Zenodo on the first release of this repository (to be added here in v1.0.1). Cite the DOI, not this repository.

## Abstract
Constitutions bind persons who took no part in making them. Jefferson held this to be a matter of force, Madison a debt that benefits justify; neither said what kind of fact it is. This article argues that it is an emergent one. A constitution is an institutional fact constituted by linguistic acts and kept in force by their inscription; once inscribed, the order acquires a property none of its components has: it binds those who took no part in its inscription. Following Andina, we call this property transgenerationality and type it as diachronic, ontological and weak emergence. Rereading the design covariates of constitutional endurance as properties of the inscription regime (who can re-inscribe a norm, by amendment or by authoritative interpretation), we then give the image of the good ancestor a precise content. The Better Ancestors Principle holds of an order if and only if every norm that binds a generation by default can be re-inscribed through a procedure that generation controls, and no body beyond its reach can re-inscribe it more cheaply. The Good Ancestors Ranking orders constitutional orders by the share of their binding norms that violate either condition. A worked example shows that the ranking can be computed from a text and a few facts about who staffs its bodies and that an eternity clause forecloses only where its reading lies beyond the generation it binds. Endurance and good ancestry come apart: an order may last precisely because its descendants cannot reach it.

## Contents
| Path | What it is |
|---|---|
| `Bourguet_2026_Better_Ancestors_preprint_v1.pdf` | The preprint (author-identified). |
| `Bourguet_2026_Better_Ancestors_preprint_v1.docx` | Same, editable. |
| `preprint.md` | Pandoc source of the preprint. |
| `source/ms_submitted_anonymous.md` | Anonymised source as submitted for review. |
| `code/gar_omega_check.py` | Recomputes the worked example (orders Ω, Ω\*, Ω′) from the definitions, plus two sensitivity orders. |
| `CITATION.cff`, `.zenodo.json` | Citation and deposit metadata. |
| `LICENSE.md` | Licence (CC BY 4.0). |

## Reproducing the worked example
The article defines the Better Ancestors Principle and the Good Ancestors Ranking so that a reader can compute the ranking from a text and a few facts about who staffs its bodies. The script does exactly that for the hypothetical orders of Section 5, with no dependencies beyond the Python standard library:

```bash
python3 code/gar_omega_check.py
```

Expected under the article's definition (rule `either`): V(Ω) = 2/3, V(Ω\*) = 0, V(Ω′) = 1/3, hence Ω\* ≻ Ω′ ≻ Ω. The script also prints a stricter reading of condition (i) and two sensitivity orders (Ω with an accessible court; Ω with a life-tenured council guarding Art. 1).

## How to cite
Bourguet, Luis. 2026. "Better Ancestors: What Constitutions Owe the Unborn." Preprint, version 1. Zenodo. DOI to be added on release.

## Versions
- v1 (2026-10-22): version submitted for peer review.
