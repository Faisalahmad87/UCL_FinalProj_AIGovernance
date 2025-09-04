# AI Fairness Mitigation  

This code repository was used for a Master's program final thesis on AI Fairness Mitigation. The title of the project is "AI Governance in Sustainable Development: A Policy Simulation". The aim of project was to understand if fairness mitigation can be developed as a governance framework that can be generalised across domains and is effective in mitigating evolving biases, thus leading research and development towards a sustainable framework for AI fairness and governance. 

## Abstract  
Ensuring fairness in artificial intelligence (AI) systems is critical for sustainable development, particularly in domains such as credit, education, and employment where algorithmic decisions impact access to essential resources. This project investigates whether a generalisable AI governance framework can detect and mitigate evolving biases across multiple datasets and domains.  

Using benchmark datasets with simulated bias shifts, we systematically evaluated a range of fairness-aware machine learning techniques, including established methods from **AIF360** and custom approaches such as **FairConsistent (FairC)**, **FairMask**, and **FairSMOTE**. Results show that no single method guarantees consistent superiority across contexts, underscoring the persistent trade-offs between fairness and predictive performance. However, **Exponentiated Gradient Reduction (EGR)** consistently performed well across domains, while FairC and FairMask demonstrated strong adaptability under evolving bias conditions, albeit with certain risks such as false positive inflation.  

Intersectional methods further revealed that single-attribute mitigation often improves fairness for one group at the expense of another, reinforcing the importance of multi-attribute and intersectional fairness audits. The study concludes that effective AI governance requires **adaptive, domain-sensitive, and intersectionally informed frameworks**, combining technical mitigation with policy and societal considerations.  

This repository provides the datasets, methods, results, and notebooks used in the project, alongside implementations of custom fairness mitigation techniques.  

---

## Repository Structure  
### Folder Details  
- **Datasets/**: Contains both original and bias-modified datasets (synthetic shifts) for all 3 domains (Adult Census, German Credit and Student Dropout). Includes raw and processed versions used in mitigation experiments.  
- **Baseline/**: Contains custom mitigation methods:  
  - *FairConsistent (FairC)* (own implementation)  
  - *FairMask* [1] (adapted from Peng et al., 2023)  
  - *FairSMOTE* [2] (adapted from Chakraborty et al., 2021)  
- **Methods/**: Contains *M3Fair* [3] for multi-attribute reweighting (intersectional mitigation).  
- **Results/**: Stores raw results from notebooks and the consolidated results used for final visualisations in the report.  
- **Notebooks/**: Jupyter notebooks for running experiments, generating modified datasets, aggregating results, and producing plots/figures.  

---

## References  

[1] Peng, K., Chakraborty, J., & Menzies, T. (2023). *FairMask: Better Fairness via Model-Based Rebalancing of Protected Attributes.* IEEE Transactions on Software Engineering. https://doi.org/10.1109/TSE.2022.3220713  

[2] Chakraborty, J., Majumder, S., & Menzies, T. (2021). *Bias in machine learning software: why? how? what to do?* In *Proceedings of the 29th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE ’21)*, 429–440. https://doi.org/10.1145/3468264.3468537  

[3] Zhu, Y., An, J., Zhou, E., An, L., Gao, J., Li, H., Feng, H., Hou, B., Tang, W., Pan, C., & Ma, L. (2023). *M³Fair: Mitigating Bias in Healthcare Data through Multi-Level and Multi-Sensitive-Attribute Reweighting Method.* arXiv preprint arXiv:2306.04118. https://arxiv.org/abs/2306.04118  

---

## Acknowledgements  

- Open-source implementations adapted from:  
  - [anonymous12138/biasmitigation](https://github.com/anonymous12138/biasmitigation)  
  - [yhzhu99/M3Fair](https://github.com/yhzhu99/M3Fair)  

---

## ⚖️ License  

This project is released under the **MIT License**. You are free to use, modify, and distribute this work, provided that proper credit is given.  

