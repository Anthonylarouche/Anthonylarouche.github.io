---
title: "Consommation et primes de risque : comment les investisseurs déterminent le prix des actifs"
subtitle: "Un cadre théorique simplifié reliant la consommation, l'utilité des investisseurs, et la tarification des actifs financiers"
layout: default
date: 2025-01-22
categories: blog
tag: [Finance]
---

{% katexmm %}

## Introduction 

Dans le cadre de ma maîtrise en statistique, j’ai eu l’opportunité d’explorer des concepts fondamentaux de la finance académique, notamment les modèles factoriels qui visent à expliquer les rendements attendus des actifs financiers. Au début, ces notions m’ont semblé complexes, ce qui m’a conduit à les reformuler dans mes propres mots pour mieux les comprendre.

Ce texte relie un modèle théorique de consommation, simplifié au maximum, à la théorie de la tarification des actifs financiers. Je commencerai par présenter les grandes lignes de ce modèle, puis j’expliquerai comment il s’applique à la détermination des prix des actifs. Enfin, je montrerai comment il mène à la représentation bêta, utilisée dans des modèles classiques comme le CAPM (Capital Asset Pricing Model) et les modèles Fama-French à 3 et 5 facteurs.

## Modèle de consommation

En général, un investisseur rationnel cherche à maximiser son utilité de manière intertemporelle. Chaque jour, il prend des décisions qui reflètent son désir de consommer maintenant ou d’épargner pour consommer plus tard. Cette dynamique peut être modélisée par l’équation d’utilité suivante :

\begin{align} \label{eq:utilite}
    U(c_t,c_{t+1}) = u(c_t) + \beta \mathbb{E}[u_{t+1}] \tag{1}
\end{align}

 - $u(c_t)$: Utilité avec le niveau de consommation actuelle

 - $\beta$: Niveau d'importance de la consommation future

 - $E[u_{t+1}]$: L'espérance d'utilité future


Une fonction d'[utilité](https://fr.wikipedia.org/wiki/Utilit%C3%A9_(%C3%A9conomie)) peut être vue comme une mesure du bien-être ou de la satisfaction, ce qui permet de donner un cadre théorique simplifié à la complexité du comportement humain. Bien que ce soit une approximation de la réalité, cette fonction permet de tirer des conclusions intéressantes. Elle est souvent monotone croissante et concave, ce qui reflète le fait que, généralement, l’utilité augmente avec la consommation. La concavité permet de capturer la décroissance de [l’utilité marginale](https://fr.wikipedia.org/wiki/Utilit%C3%A9_marginale#:~:text=L'utilit%C3%A9%20marginale%20est%20d%C3%A9croissante,et%20d'autres%20objets%20divers.), c’est-à-dire que la satisfaction liée à chaque unité de consommation supplémentaire diminue. Par exemple, le bonheur d’avoir une première assiette de ton plat préféré est bien plus grand que celui d’en manger une dixième.

L’équation \ref{eq:utilite} nous indique que pour maximiser son utilité, il faut prendre en compte la consommation future. Supposons qu’aujourd’hui nous avons un potentiel de consommation $\gamma_t$ et que nous souhaitons savoir combien investir ($\xi$) à un prix $P_t$. Il suffit alors de maximiser la fonction (1) avec les contraintes suivantes :

$$
c_t = \gamma_t - P_t \xi \\
c_{t+1} = \gamma_t + x_{t+1} \xi
$$

On remplace $c_t$ et $c_{t+1}$ par les contraintes et dérivons par rapport à $\xi$. On égalise la dérivé à 0 et ensuite on isole $P_t$, afin d'obtenir une expression de prix. Le résultat est le suivant :

$$
P_t = E_t \left [\beta \frac{u'(c_{t+1})}{u'(c_t)}x_{t+1} \right ] \tag{2}
$$

L’équation (2) montre que si l’investisseur valorise davantage la consommation future, son utilité marginale sera plus grande pour la consommation future que pour la consommation actuelle. Avec un $\beta$ fixe, la constante d'actualisation sera plus élevée et l'investisseur sera prêt à payer plus cher pour un actif qui lui garantit des flux d’argent futurs. Par exemple, si vous prévoyez prendre votre retraite dans 5 ans, vous risquez de diminuer votre consommation, mais vous la valoriserez davantage et serez moins enclin à prendre des risques. Vous opterez probablement pour un actif sans risque.

À l’inverse, si vous prévoyez une consommation plus élevée à l’avenir qu’aujourd’hui, l’inverse se produit : $u'(c_t) > u'(c_{t+1})$. La constante d’actualisation des gains sera plus faible et l’investisseur sera prêt à payer moins cher pour un actif plus risqué, afin d’atteindre son objectif de consommation. Si, par exemple, vous avez un horizon de travail de 25 à 35 ans, vous serez plus enclin à prendre des risques pour augmenter votre consommation future.

Dans la littérature, il est commun d'appeler la constante d'actualisation des gains le *stochastic discount factor*. Dans plusieurs articles, ceci réfère à la variable $M_{t+1}$. Alors, la représentation finale du prix est la suivante, 

$$
P_{i,t} = E\left[M_{t+1}x_{t+1}\right].
$$

## Le prix est une prédiction

À partir de maintenant, simplifions l'équation du prix en retirant les indices temporelles.

$$
P_{i} = E[Mx]
$$

Le prix $P_i$ est toujours exprimé à un instant $t$, sauf indication contraire, et $E_t$ est conditionné par l’information disponible à cet instant. De même, $M_{t+1}$ et $X_{t+1}$ sont inconnus et se réfèrent à des valeurs futures.

Comme le mentionnent Kelly et Xiu (2023), le prix représente la prédiction des investisseurs qui utilisent toutes les informations disponibles au temps $t$. Le prix d’un actif $i$ à l'instant $t$ est donc une estimation des gains futurs $X_{t+1}$ actualisés au temps $t$ à l’aide du *stochastic discount factor*.

Pour des raisons techniques, il est souhaitable de travailler sur une même échelle en normalisant les gains futures par le prix.

$$
R_{i} = \frac{X_{i,t+1}}{P_{i}},
$$

est nul autre que le rendement brut de l'actif $i$ pour la période $t$ à $t+1$.

Comme le souligne Cochrane (2009), un rendement brut peut être interprété comme un actif ayant un prix de 1 dans l’équation suivante :

$$
1 = E[mR] \tag{3}
$$

À partir de l’équation (3), nous pouvons lier le stochastic discount factor au taux de l’actif sans risque. En effet, étant donné qu’il n’y a pas de "risque" ou de variation dans le rendement $R_f$, la propriété de la linéarisation de l'espérance nous permet de sortir la constante $R_f$ de l'équation $1 = E[m]R_f$. Il suffit d'isoler et nous retrouvons l'identité suivante,
$$
R_f = \frac{1}{E[m]} \tag{4}
$$

On peut se demander comment $m$ varie avec les gains $x$. En général, un actif plus risqué devrait bien performer lorsque l’économie se porte bien, et ainsi, être corrélé positivement avec la consommation. Cependant, étant donné que l’utilité marginale décroît avec l’augmentation de la consommation, le stochastic discount factor aura une relation négative avec les gains futurs d’un actif. Examinons de plus près l’équation de la covariance :
$$
cov(m,x) = E(mx) - E(m)E(x) \\
 \rightarrow E(mx) = E(m)E(x) + cov(m,x) \\
 \rightarrow P = E(m)E(x) + cov(m,x) \\
 \rightarrow P = \frac{E(x)}{R_f} + cov(m,x)
$$

Nous retrouvons ici l’expression du prix, qui repose sur deux éléments : le prix des gains futurs actualisés par le taux sans risque, et l’ajustement en fonction du risque via la covariance. Comme mentionné précédemment, la covariance entre $m$ et $x$ sera négative pour les actifs risqués. Le prix sera donc ajusté en fonction du risque et l’investisseur paiera un prix inférieur pour un actif risqué par rapport à un actif sans risque. Si nous exprimons cela en termes de rendement, en divisant par le prix $P$ et en réarrangeant les termes, nous obtenons :

$$
R_i - R_f = -R_fcov(m,R_i)
$$

Le rendement excédentaire de l’actif $i$ est donc expliqué par $-R_fcov(m,R_i)$. Cela est cohérent avec notre description précédente : la partie droite de l’équation sera positive lorsque la covariance est négative. En remplaçant $R_f$ par l’expression de l’équation (4), 

$$
R_i  =R_f -\frac{cov(m,R_i)}{E(m)}.
$$


## Représentation Bêta

En finance académique, la notion de représentation bêta est utilisée pour décomposer le rendement excédentaire d'un actif en deux composantes clés : la quantité de risque et le prix du risque. Cela nous permet d'interpréter les résultats de manière plus intuitive.

L’équation suivante reformule la relation entre le rendement excédentaire attendu et le stochastic discount factor :

$$
R_i  =R_f + \frac{cov(m,R_i)}{var(m)}\left(-\frac{var(m)}{E(m)}\right).
$$

Dans cette expression :  
- $\frac{\displaystyle \text{cov}(m, R_i)}{\displaystyle \text{var}(m)}$ représente la **quantité de risque**, c’est-à-dire la sensibilité du rendement d’un actif $R_i$ au stochastic discount factor $m$.  
- $-\frac{\displaystyle \text{var}(m)}{\displaystyle E(m)}$ correspond au **prix du risque**, c’est-à-dire la compensation requise pour assumer ce risque.  

En d'autres termes, cette décomposition nous montre que le rendement excédentaire d’un actif dépend de sa sensibilité au risque systématique (quantité de risque) et du coût associé à ce risque (prix du risque).

Cela conduit à une version plus courante de cette relation : 

$
E(R_i) - R_f = \beta_{i,m} \lambda_m,
$

où :  
- $\beta_{i,m} = \frac{\text{cov}(m, R_i)}{\text{var}(m)}$  
- $\lambda_m = -\frac{\text{var}(m)}{E(m)}$ 

Cette représentation met en évidence que les investisseurs exigent une prime $\lambda_m$ pour les actifs présentant une corrélation élevée avec les facteurs de risque.

### Le CAPM : un premier modèle bêta

Le **Capital Asset Pricing Model** (CAPM), introduit par Sharpe (1964), repose sur l'idée qu'un seul facteur explique les rendements excédentaires des actifs : le risque du marché. L’équation du modèle s’écrit comme suit :

$$
E(R_i) - R_f = \beta_{i,m} \lambda_m,
$$

où :  
- $\beta_{i,m}$ est la sensibilité du rendement de l’actif $i$ au facteur de risque marché.  
- $\lambda_m$ est la prime de risque associée au marché.  

Dans ce cadre, un actif avec un \(\beta_{i,m}\) élevé est considéré comme plus risqué et doit offrir un rendement excédentaire plus élevé pour compenser ce risque.

Cependant, des études comme celles de Fama et MacBeth (1973) ont montré que les résultats empiriques du CAPM sont souvent faibles. Les primes de risque associées aux $\beta_{i,m}$ ne sont pas toujours significatives, ce qui a motivé la recherche de modèles plus complexes.



### Fama-French : des modèles à plusieurs facteurs

En réponse aux limites du CAPM, Fama et French (1993) ont proposé un modèle à trois facteurs, qui inclut deux nouveaux risques systématiques :  
1. **SMB (Small Minus Big)** : une prime liée à la taille des entreprises, mesurée par leur capitalisation boursière.  
2. **HML (High Minus Low)** : une prime liée à la valeur des entreprises, mesurée par leur ratio valeur comptable/valeur de marché.

L’équation s’écrit alors :

$$
E(R_i) - R_f = \beta_{i,m} \lambda_m + \beta_{i,SMB} \lambda_{SMB} + \beta_{i,HML} \lambda_{HML}.
$$

Ce modèle permet d'expliquer entre 70 % et 90 % des variations des rendements excédentaires, une amélioration significative par rapport au CAPM.

En 2015, Fama et French ont étendu leur modèle à cinq facteurs, en ajoutant :  
- **RMW (Robust Minus Weak)** : une prime liée à la profitabilité.  
- **CMA (Conservative Minus Aggressive)** : une prime liée aux stratégies d’investissement des entreprises.  

Avec ce modèle, ils parviennent à expliquer jusqu’à 95 % des variations des rendements excédentaires.


### Le "zoo des facteurs"

Au fil du temps, la recherche a identifié des centaines de nouveaux facteurs, donnant naissance au **"factor zoo"**. Ce terme décrit la prolifération des facteurs prétendument significatifs pour expliquer les rendements excédentaires. Toutefois, de nombreux facteurs sont redondants ou reposent sur des biais statistiques.

L'article "Taming the Factor Zoo: A Test of New Factors" propose une méthodologie rigoureuse pour évaluer la pertinence marginale des nouveaux facteurs, en insistant sur l'importance d'une approche empirique robuste.

## Conclusion 



{% endkatexmm %}


