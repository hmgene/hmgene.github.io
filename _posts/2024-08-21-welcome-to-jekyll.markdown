---
layout: post
title:  "Journal-Club: Macrophage-mediated myelin recycling fuels brain
cancer malignancy, Kloosterman2024Cell"
date:   2024-08-21 15:24:57 -0400
categories: journal-club
---
![image](https://github.com/user-attachments/assets/96d4a943-3913-491f-b712-46c28b58915f)

>Myelin (/ˈmaɪ.əlɪn/ MY-ə-lin) is a lipid-rich material that surrounds nerve cell axons (the nervous system's electrical wires) to insulate them and increase the rate at which electrical impulses (called action potentials) pass along the axon.[1][2] (wikipedia) 

## Highlights
![image](https://github.com/user-attachments/assets/e66f9655-9d11-4c48-b001-46552f4b4105)
1. TAM recycle cholesterol-rich myelin, **lipid-laden** features in glioblastoma
2. Epigenetic rewiring by myelin debris scavenging underlies LLM **immunosuppressive** feature

## Summary:
Heterogeneity of the glioiblastoma TME using single-cell and multi-omics 
=> rewired TAM subpopulations => LLMs transfer myelin-derived lipids to cancer cells
=> LLM-rewired pro-tumoric and immunosuppresive features in MES
 
## Results
### Murine glioblastoma displays dynamic cellular subtype heterogeneity in response to RT
Genetically engineered mouse models (GEMMS):
- Ink4a (CDKN2A) : tumor suppressor gene that encodes a protein involved in regulating the cell cycle.
- Arf : tumor suppressor, control cell proliferation by stabilizing p53, a tumor suppressor
- scRNA-seq : CD45+- x Primary,recurrent after RT 
![image](https://github.com/user-attachments/assets/edfc518b-9084-400d-a76c-bfae0a88e930)

Cellular Subtypes: 
- neural progenitor-like (NPC-like)
- oligodendrocyte-progenitorlike (OPC-like)
- astrocyte-like (AC-like)
- MES-like—is represented
![image](https://github.com/user-attachments/assets/c670c876-d8e1-4e6b-af80-3b9bb1601922)

Gliblastoma Atlas Project (GAP) datasets, niche-specific anatomic signatures (Fig1D) :
- LE, leading edge; CT, cellular tumor; MVP, micro-vascular proliferation; PAN, pseudo-palisading cells around necrosis

Intra-tumor heterogeneity primary/recurrent post-RT (Fig1D) :
- PDG-p53 : AC-like => OPC-like
- PDG-Ink4a : OPC-like => MES-like
- in a stage and niche-dependent manner, mirroring results reported in glioblastoma patients

### Macrophage subset dynamics correlate with glioblastoma stage, cellular subtype composition, and local niches
- 4 Microglia(MG) and 4 MDM (Monocyte-Derived Macrophage)
- MG1-P2RY12 : pre-active
- MG2-TNF, MDM2-H2-EB1 : inflammatory
- MG3/MDM3-GPNMB : metabolically active
![image](https://github.com/user-attachments/assets/019f8436-6463-44a4-9175-e319720a985f)
  
- MG4/MDM4-MKI67 : proliferating states, MES-like (Fig1H)
- ? *MG1 : preactivated ~ helthy brain at LE, tumor invasion into brain parenchyma from which MG originate *
- MDM1 : preactivated infiltrating the tumor site in MVP area (Fig1G)

![image](https://github.com/user-attachments/assets/796df034-1652-4a41-a8d2-d4ba0c6fc253)

  
In summary, we present in-depth functional analyses of a protumorigenic
LLM subset in glioblastoma, spanning from studying
their transcriptional education and chromatin alterations to their
re-configured lipidome. We reveal that lipid-laden-TAMs’ pro-tumoral
functions are largely driven by the excessive, TME-instructed
uptake of myelin debris.

Key Questions:

- in multiple sclerosis, showing myelinphagocytosis in macrophages directly dampens T cell proliferation and neuroinflammation.43,68
Surprisingly, however,
- targeting LLMs in vivo did not lead to overt changes in lymphoid populations frequency in end-stage tumors. In light of the controversial roles lipids play in immune activation,69

- adaptive mechanisms supportive of glioblastoma relapse post-therapy.
- suggest MES-like glioblastoma cells rely heavily on local cholesterol metabolism
- LLMs display immunosuppressive features and negatively correlate with response to ICB
You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
