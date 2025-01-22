---
title: Fama-Macbeth regression
subtitle: Factor's loadings estiamtion 
layout: default
date: 2025-01-21
categories: blog
tag: [Finance]
---

## Contexte d'utilisation

La régression Fama-Macbeth est utilisé dans un contexte ou nous cherchons à estimer un coeficient $\lambda_t^f$ , c'est-à-dire, la compensation
associée à un facteur de risque $\beta_i^f$. Plus formellement, nous retrouvons la forme suivante :

$$
r_{i,t} = \alpha_i + \lambda_t^f\beta_{i,t}^f + \varepsilon_{i,t}
$$

À première vue, c'est un problème de régression simple ou multiple qui se résoud facilement. Cependant, je me souviens d'avoir été choqué de réalisé qu'en réalité nous n'avons même pas nos variables indépendantes afin de résoudre ce simple OLS. En ce sens, il nous faut une méthode empirique afin d'estimer nos variables "indépendantes".

En 1973, Eugene F. Fama et James D. MacBeth ont publiés un article intitulé *Risk, Return, and Equilibrium: Empirical Tests*.
L'idée était de tester 3 hypothèses fondamentales concernant les marché financiers. 

 - Le lien entre le rendement et le risque est linéaire
 - Aucun risque autre que le risque de l'actif peut générer un rendement excédentaire
 - La différence de rendement espéré entre un actif risqué et un actif sans risque est positive

En voulant répondre à ces hypothèses, ils ont du développer une technique empirique afin d'estimer les coefficients $\beta$s pour ensuite bien estimer la significativité des compensations de risques $\lambda$. Par exemple, si nous prenons le CAPM, ce modèle nous dit que le risque est l'unique raison qu'un actif reçois une compensation plus élevé en moyenne que l'actif sans risque. Pour ce faire, nous devons calculer chaque coefficients $\beta$ sur une période de temps $T$. 

### Étape 0
À cette étape, nous calculons les facteurs de risque ou les caractéristiques que nous voulons tester. Ces caractéristiques peuvent être la grosseur de l'entreprise (Market value), le Book-to-market ou encore le P/E. Dans le cas du facteur de risque du marché, comme le stipule le CAPM, nous procèderions au calcul des $\beta$ dans une régression temporelle. L'équation serait la suivante :

$$
R_{i,t} - R_{f,t} = \alpha_i + (R_{m,t} - R_{f,t})\beta_i + \varepsilon_{i,t}
$$

Nous calculons une régression temporelle par actif afin d'estimer le $\beta_i$ spécifique pour chaque action.

### Étape 1

Maintenant, il est possible de constuire des portefeuilles ou de faire cette estimation sur les actifs individuels. Dans tout les cas, nous procédons à une régression tranversale, c'est-à-dire, les variables dépendantes sont maintenant les $R_{i,t}$ pour un $t$ fixe et les variables indépendantes sont les $\beta$s calculés à l'étape 0. 

$$
R_{i,t} = \gamma_t + \lambda_t\beta_{i,t} + \eta_t
$$

Il y a donc $T$ regressions et $T$ $\lambda$.
### Étape 2

Avec l'estimation des $\lambda$ de l'étape 1, nous pouvons faire une moyenne et calculer son erreur-type.


$\bar{\hat{\lambda}} = \frac{\sum_{t=1}^{T} \hat{\lambda}_t}{T}$

$\sigma(\bar{\hat{\lambda}}) = \sqrt{\frac{\sum_{t=1}^{T} (\hat{\lambda}_t- \bar{\hat{\lambda}} )^2}{T-1}}$ # note : manque un T  quelque part


## Exemple en R

