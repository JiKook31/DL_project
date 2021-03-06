# STAP: Simultaneous Translation And Paraphrase

[![CI](https://github.com/JiKook31/DL_project/workflows/CI/badge.svg)](https://github.com/JiKook31/DL_project/actions?query=workflow%3ACI)

Machine translation systems typically produce a **single output**, but in certain cases, it is desirable to have **many possible translations** of a given input text.

The **goal** is to use Deep Learning models and generate high-coverage set of plausible translations from English to Russian. 

The outcomes will be:

-   New **translation datasets** provided to the community
-   New **benchmarks** for Machine Translation and paraphrasing

**Ideal result representation:**
> **Погожим летним вечером она танцевала под музыку.**

* On a fine summer evening, she danced to music.
* A female waltzed to music on a serene summer evening.
* She moved with a rhytm as the summer day declined.

## Tools
**Language** - Python 3\
**VCS** - GitHub\
**Board** - GitHub project board\
**Report writing** - HackMD\
**Communication** - Telegram\
**Documents storage** - Google Drive

## Agile organization
**Roles:** \
Product owner: Vladimir Ivanov \
Scrum master: Alternating b/w Alina and Alsu \
Development team: Alina, Alsu + 2 other students 
1. Sprint 0: laying out **product backlog** (collecting user stories).
2. **Sprint planning**\
	2.1 Discuss *user stories* to be moved from the Product backlog to the **sprint backlog**.\
	2.2. Prepare sprint backlog. Distribute stories, bugs, tasks.\
	2.3. Agree on **goal** of sprint.
3. **Daily Standups**\
	3.1. Each team meber gives answers to three questions:\
		* What have I done yesterday that will make the team closer to the sprint goal?\
		* What are my plans for today?\
		* Do I see any problems with reaching sprint goal?\
	3.2. All problems shall be recorded by the Scrum master and placed on the organisation board under "Risks" column.
4. **Spring review + retrospective**\
	4.1. The team reviews completed/failed tasks.\
	4.5. "Presenting" work for the "stakeholders": writing a report for the professor.\
	4.6. Reflecting on the past sprint: what went right, what went wrong, what could be improved.

**Product backlog** is available [in this document.](https://docs.google.com/document/d/1oadHdlKemfdsWWG--NHEUlqlxM8VoyWGKKxPRNUK_io/edit?usp=sharing)

## Progress

### Sprint 6 burndown chart
![resources](https://docs.google.com/spreadsheets/d/e/2PACX-1vQCSDKOa81TX43Hge2rS20bQrY0QDnXLxYFWPjh4HEBgoPcogHZfafJJf5Bx54Bm9NaTSAHJJw8tHyg/pubchart?oid=1591942575&format=image)

## Evaluation chart

<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSHDLY6gFINy8nBgLJb81mLj9IkczivmAyML4zdw_dxAN6vNRxIOuSpkBkKgUA4ixQG_P8MFCwEXwbY/pubchart?oid=1546331004&amp;format=image">
</img>

## Quality Assessment

The project was evaluated using Bilingual Evaluation Understudy (BLEU) score. BLEU score is a metric for evaluating a generated sentence to a reference sentence.

Final scores are:
* translation model: 51.0,
* paraphrase model: 29.0.

In other words, we achieved roughly State-Of-The-Art results in both of the models.

Additionally, the accuracy of the model is regularly tested. It should be more than 75% after every commit.

## Added Value

The biggest value that was added for business is Telegram Bot that can translate Russian sentence into multiple English ones. Example of our bot can be seen below:

<img src="https://camo.githubusercontent.com/890b1b89d7d075c05b0a7fef63af971a166cd485/68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f4c2d6949395a494166747765533138303571656e417355446e3736446766745f762d3568746573474b2d646a764d752d44356f6e6436467a71446432734e444e4f6a684157347449394e613476786d41506b6a4d5777434a5249776a5266424d562d4f7059344475386157434b374e4a52535f693172695075474672544c355266757571493877794c61774b6656433150674947586c44693439416a2d69673859506856346e4634323972315f6856416d385a754464785479547a666c31615832755438535a67466d6e4547774543486e45786a595f6c4a695347704c565447776a6e654c355a31306e4241564d485258553138476b333546464131706a4c4457587132686f365761776b4e447176354771334159496b316930726c4d344c79554b42453738644f6c43724e41317554622d3954634c384c39507279354b51705777306f50344f5149486f68593336693434734366656f766f655164547a41536c4f56563044354a2d5a31514e4d465173494b385462544b6b5f5967686f72334761674a3036492d54617833674e3431715548314a6a76616a6a396f556c6864573961544d3975766768325855705333504c52496f6d493954354b584a4f4357555453534b32395a325733697a564c7943794553324a7567433659677473637a5a6f657068744c303957342d31663362316b42553539535a564f596d71775461442d4e6f48354a756f6571765a776d64496c695a6e5f7542746d31414946492d3839735165643856524646525748354b7a793577365531305a4a6746466863566a78354e7a52596153687161564b4c63612d347275794774684a6239724b4a6a616e524444563565684e69354e7538496367334c68766e4a6b474549623064577644557a46687977523179345535537834596b4838654e5475624a6b395f69797864524676486b7a7752665a78466349454a4d654143366c6b495066702d61315447613034413d77323838302d68313539362d6674" data-canonical-src="https://lh3.googleusercontent.com/L-iI9ZIAftweS1805qenAsUDn76Dgft_v-5htesGK-djvMu-D5ond6FzqDd2sNDNOjhAW4tI9Na4vxmAPkjMWwCJRIwjRfBMV-OpY4Du8aWCK7NJRS_i1riPuGFrTL5RfuuqI8wyLawKfVC1PgIGXlDi49Aj-ig8YPhV4nF429r1_hVAm8ZuDdxTyTzfl1aX2uT8SZgFmnEGwECHnExjY_lJiSGpLVTGwjneL5Z10nBAVMHRXU18Gk35FFA1pjLDWXq2ho6WawkNDqv5Gq3AYIk1i0rlM4LyUKBE78dOlCrNA1uTb-9TcL8L9Pry5KQpWw0oP4OQIHohY36i44sCfeovoeQdTzASlOVV0D5J-Z1QNMFQsIK8TbTKk_Yghor3GagJ06I-Tax3gN41qUH1Jjvajj9oUlhdW9aTM9uvgh2XUpS3PLRIomI9T5KXJOCWUTSSK29Z2W3izVLyCyES2JugC6YgtsczZoephtL09W4-1f3b1kBU59SZVOYmqwTaD-NoH5JuoeqvZwmdIliZn_uBtm1AIFI-89sQed8VRFFRWH5Kzy5w6U10ZJgFFhcVjx5NzRYaShqaVKLca-4ruyGthJb9rKJjanRDDV5ehNi5Nu8Icg3LhvnJkGEIb0dWvDUzFhywR1y4U5Sx4YkH8eNTubJk9_iyxdRFvHkzwRfZxFcIEJMeAC6lkIPfp-a1TGa04A=w2880-h1596-ft" width="210" height="400" />
