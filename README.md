# Web Scraping and APIs for Humanities Research

*Сourse materials*

The second course of the [Minidegree Digital Humanities](https://github.com/Minidegree-DH) programme, Faculty of Humanities, HSE University, 2026/27. Teaching language: Russian.

📖 **Course website:** <https://minidegree-dh.github.io/miniDH-scraping/>

## About the course

Students learn to collect data for humanities research with Python: how HTTP and web APIs work, how to extract data from static and dynamic web pages, how to query Wikidata with SPARQL, and how to turn the result into a clean, documented dataset. Ethical and legal aspects of data collection are discussed throughout the course.

The course builds on *Digital Technologies in Professional Practice* ([minidh-intro](https://github.com/Minidegree-DH/minidh-intro)) and prepares data-collection skills for *Natural Language Processing & Computer Vision* ([miniDH-NLP-CV](https://github.com/Minidegree-DH/miniDH-NLP-CV)).

## Repository structure

```
├── 01_seminar/ … 07_seminar/   # notebooks, slides and small datasets for each session
├── project/                    # final project requirements and templates
├── site/                       # Quarto sources of the course website
├── docs/                       # rendered website (served by GitHub Pages)
├── requirements.txt
└── LICENSE
```

## Getting started

Requires Python 3.11 or newer.

```bash
git clone https://github.com/Minidegree-DH/miniDH-scraping.git
cd miniDH-scraping
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Open the folder in VS Code and select the `.venv` interpreter as the notebook kernel. Detailed instructions (in Russian) are on the [setup page](https://minidegree-dh.github.io/miniDH-scraping/setup.html).

## Updating the website

```bash
cd site
quarto render        # writes the website to ../docs
```

Commit `site/` and `docs/` together. Do not edit files in `docs/` by hand.

## License

Course materials are licensed under [CC BY 4.0](LICENSE). Materials adapted from third-party sources keep their original licenses; such files are marked in their headers.
