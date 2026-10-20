# CSS networks in Latin America: research protocol

Author: Sol Zoe Nottage. Version: October 20, 2026. Status: ongoing, incomplete coverage.

## Scope and eligibility

The directory records people, institutions, programs, events and publications linked to computational approaches to social phenomena, humanities, education, government and public policy. A general AI or data-science program does not qualify without a documented social application. Public-data portals, public-sector analytics teams and government laboratories are included as applied social data or public-data infrastructure. Inclusion does not automatically establish academic CSS research.

Teaching in an eligible program or speaking at an eligible event establishes that participation, not an individual's research specialization, permanent employment or residence. Institutional location is distinguished from nationality and personal address. Historical cohorts and appointments retain their documented period.

## Country-by-country review

1. Establish the institutional frame from an official national university register. Record the edition and reconcile names, branches, openings and closures.
2. Locate each official website and review degree programs, postgraduate programs, certificates, continuing education and relevant academic units.
3. Check candidate programs against the explicit social-application criterion. Read curricula, faculty lists and cohort dates.
4. Review seminars, talks, news and events. Record speakers, organizers, roles and dates.
5. Follow documented research centers, laboratories, partner institutions, think tanks and consultancies.
6. Verify individual identities and publications. Retain source URLs, consultation dates, decisions, exclusions and unresolved cases.

Public-sector review follows a complementary frame: national agencies, provinces or states, and municipalities. Portals, responsible agencies, projects and staff are distinguished. Think tanks and consultancies are identified through directories and documented institutional links; this open frame is not claimed to be exhaustive.

A preliminary automated crawl identifies candidate pages only. A download, keyword match or inaccessible page does not complete an institutional review. Review states distinguish pending, in progress, partial, reviewed with findings, reviewed without findings in the consulted sources, and inaccessible. Countries remain incomplete while the frame or institutional reviews are unresolved.

## Current inventory limitations

The initial South American inventory combines national or institutional lists from Argentina, Chile, Colombia, Ecuador, Peru and Paraguay with candidate domains from Hipo's university directory. The latter is neither an official register nor an exhaustive list. The Colombian dataset retrieved reports a 2022 update. The Argentine government PDF is a 2024 edition and requires reconciliation with subsequent changes.

Exact country and normalized-name matching removes simple case and accent differences. Unresolved abbreviations, translations and aliases remain separate. Therefore, inventory rows must not be interpreted as a count of unique universities. Program and team reviews are tracked separately from institution discovery. Guyana and Suriname are included in the geographic South American stage, distinguished from the Latin American linguistic scope.

## Sources and validation

Evidence comes from institutional websites, program pages, repositories, publications, arXiv and Crossref metadata. Google Scholar was attempted but was unavailable for automated extraction; it is not described as an extracted source. Retrieved titles and authors are checked against the intended reference. False matches are excluded. Duplicate versions of a work require consolidation, using DOI and bibliographic evidence. Ambiguous identities are not merged solely because their names are similar. Email addresses and LinkedIn profiles are not guessed.

## Relationships and network analysis

Affiliation, teaching, event participation, public roles and coauthorship are distinct relationships. Sharing an institution, program or event does not establish coauthorship. Institutional publication links use the affiliations documented in the paper, not authors' current affiliations.

The coauthorship graph is undirected, without self-loops. Edge weight counts shared works. Degree counts distinct coauthors; strength sums weights. Betweenness uses unweighted shortest paths and is normalized. Weighted eigenvector centrality is calculated within the largest connected component. Communities use weighted Louvain, resolution 1 and seed 42.

Displayed dashboard counts and report text are recalculated for the active filters. Coauthorship metrics use selected authors and edges with both endpoints selected. Publication counts include works with at least one selected author. The affiliation view may retain adjacent institutions as context. The saved network file also retains full-corpus metrics. Report charts remain aggregate; individual names are available in the directory, not as prestige rankings in the report.

## Planned subnational concentration analysis

This analysis is pending location verification. It will use documented institutional locations, not assumed residences or the location of a university offering a remote course. Missing and ambiguous locations will remain explicit.

People, institutions and initiatives will be counted separately. For geolocated records, a place's share is its count divided by all geolocated records in the selected country and unit of analysis. The Herfindahl index is the sum of squared location shares. Multiple-location records require a documented allocation rule before estimation; fractional allocation is the planned rule. Geographic coverage and the proportion of unlocated records must accompany the results. These measures describe the observed directory, not the actual concentration of the entire field.

## Reproduction and submissions

The repository includes data, source references, exclusions and scripts. `build_network.py` checks the coauthorship projection against corpus author lists. `build_inventory.py` reconstructs the provisional inventory from downloaded inputs. External pages can change, so new downloads do not guarantee identical historical output. The source manifest records hashes of original downloads.

The public GitHub form accepts proposed profiles, institutions, programs and corrections. Submissions require sources and review before inclusion; they do not automatically change dashboard counts. No individuals were contacted.

## Authorship and AI assistance

Sol Zoe Nottage is the author. ChatGPT, through Codex, assisted source discovery, extraction-script development, processing, analysis implementation and website development. Generated responses are not evidence of a person's role or affiliation. The tool is not a coauthor.

OpenAI. (2026). *ChatGPT* [AI tool used through Codex]. https://chatgpt.com/ . Use documented on October 20, 2026; no specific model version is asserted.
