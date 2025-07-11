---
title: L'échec empirique du CAPM
subtitle: Le CAPM demeure le modèle privilégié pour enseigner la relation fondamentale entre risque et rendement. Pourtant, peu d’attention est généralement portée à son estimation pratique et à sa validité empirique. Dans ce texte, j’explore l’une des méthodologies les plus répandues en finance empirique, soit la régression de Fama-MacBeth. Je mets en lumière les principales difficultés rencontrées par les chercheurs pour estimer rigoureusement les primes de risque.
layout: default
date: 2025-07-02
categories: blog
tag: [Finance]
---
{% katexmm %}
## Mise en contexte

Les modèles factoriels occupent une place centrale dans l’évaluation des actifs financiers. Parmi eux, le *Capital Asset Pricing Model (CAPM)* occupe une place à part. À la fois simple, élégant et ancré dans une intuition forte, ce modèle repose sur l'idée que plus un actif est exposé au risque du marché, plus le rendement que les investisseurs en attendent doit être élevé. Cette compensation est la prime de risque ou encore, le prix par unité de risque associé au risque systématique du marché.

Sur papier, le CAPM a tout pour plaire. Mais lorsqu’on le confronte aux données réelles, les choses se compliquent. D’importants défis statistiques apparaissent, remettant en question sa validité empirique.

Dans ce texte, je vous propose de :

1. revenir sur l’intuition et la structure du CAPM ;
2. explorer les limites rencontrées dans les premiers tests empiriques du modèle ;
3. découvrir la méthode **Fama-MacBeth**, une approche simple et ingénieuse pour estimer les primes de risque malgré les difficultés rencontrées avec les données financières.


## Le CAPM : un modèle fondateur

Dans les années 1950, Harry Markowitz bouleverse la manière de penser les portefeuilles d’investissement en introduisant l’analyse moyenne-variance (*mean-variance analysis*). Son idée est simple : un investisseur rationnel devrait chercher à maximiser le rendement attendu de son portefeuille, pour un niveau de risque donné, mesuré par sa volatilité. Cette approche devient la pierre angulaire de la théorie moderne du portefeuille.

Une dizaine d’années plus tard, William Sharpe (1964), bientôt rejoint par Lintner (1965) et Mossin (1966), pousse plus loin cette logique. Ils introduisent la notion de risque systématique : seul le risque lié aux mouvements globaux du marché devrait, selon eux, être récompensé. La première version du CAPM voit alors le jour.

Ce modèle nous dit que les différences de rendement entre les actifs ne s’expliquent que par leur sensibilité au marché, mesurée par un coefficient appelé **bêta**. Autrement dit, ce n’est pas le risque total d’un actif qui compte, mais uniquement la part de ce risque que l’on ne peut pas diversifier.


La version Sharpe-Linter du modèle s'écrit :
\[
E[R_i] - R_f = \beta_i (E[R_M] - R_f) \tag{1}
\]

Où :

- $E[R_i] $ : rendement espéré de l’actif *i*
- $ R_f $ : taux sans risque
- $ \beta_i $ : sensibilité de l’actif *i* au portefeuille de marché
- $ E[R_M] $ : rendement espéré du marché

En d'autres mots, le rendement excédentaire espéré d’un actif est une fonction linéaire du rendement excédentaire du marché. 

En théorie, le CAPM est un outil pédagogique remarquable pour illustrer le lien fondamental entre risque et rendement. Mais une question cruciale demeure : le modèle tient-il la route face aux données ? Et surtout, comment l’estimer rigoureusement, sachant que les $\beta_i $ et $ E[R_M] - R_f$ doivent eux-mêmes être estimés à partir des données observées ?


## Les premiers tests empiriques du CAPM

Les premières validations empiriques du CAPM (Sharpe-linter) reposent sur trois implications fondamentales du modèle :

1. Le rendement espéré d’un actif dépend uniquement de son bêta, aucune autre variable ne devrait expliquer les différences de rendement.
2. La relation entre bêta et rendement espéré est linéaire et croissante : un actif plus risqué (au sens du bêta) doit offrir un rendement plus élevé.
3. Un actif avec un bêta nul devrait offrir un rendement égal au taux sans risque.

Les premiers tests empiriques se concentraient surtout sur les points 2 et 3, en particulier la validité de la relation linéaire entre bêta et rendement, ainsi que la valeur de l’ordonnée à l’origine. Or, dans la plupart des cas, cette ordonnée ne correspondait pas au taux sans risque, comme le prédit le modèle de Sharpe-Lintner.

Ce rejet ne signifie pas pour autant que l’intuition générale du CAPM est invalide. Il indique plutôt que la version spécifique proposée par Sharpe-Lintner, avec ses hypothèses strictes, ne résiste pas aux données.

D’autres versions du CAPM, comme celle proposée par Black (1972), assouplissent les hypothèses du modèle de Sharpe-Lintner. Par exemple, elles ne supposent pas que l’ordonnée à l’origine soit égale au taux sans risque, mais plutôt qu’elle corresponde au rendement d’un actif fictif ayant un bêta nul, ce qu’on appelle le *zero-beta security*.

Ces versions alternatives ont l’avantage de permettre des tests plus souples de l’idée centrale du modèle : le lien entre risque systématique et rendement. Cela dit, il reste très difficile de confirmer ou d’infirmer empiriquement le CAPM, même dans ses formes assouplies.

Le principal obstacle est le portefeuille de marché lui-même. En pratique, nous n’observons jamais le vrai portefeuille de tous les actifs existants. Faut-il y inclure le capital humain ? L’immobilier ? Les actifs non cotés ? Ces questions n’ont pas de réponse simple.

C’est pourquoi les chercheurs utilisent des *proxies* pour le marché, comme un portefeuille pondéré des actions américaines cotées, basé sur leur capitalisation boursière. Cette approximation est pratique, mais elle reste imparfaite et c’est l’une des limites fondamentales de tous les tests empiriques du CAPM.

## Les premières estimations

Les premiers tests utilisaient une stratégie en deux étapes :

### Étape 1: Estimation des bêtas individuels via une régression temporelle 

Cette étape consiste à régresser les rendements de l'actif $i$ sur les rendements du marché. De cette façon, l'estimation représente la partie de l'actif exprimé par le marché. En d'autres mots, la sensibilité de l'actif au marché.
$$
R_i = \alpha_i + \beta_i R_M + \epsilon_i \tag{2}
$$

avec :

- $R_i \in \mathbb{R}^{T \times 1}$ : vecteur des rendements de l’actif $i$ observés sur $T$ périodes ;
- $\alpha_i \in \mathbb{R}$ : constante représentant la partie du rendement non expliquée par le facteur de marché ;
- $\beta_i \in \mathbb{R}$ : sensibilité de l’actif $i$ au rendement du marché (coefficient de régression) ;
- $R_M \in \mathbb{R}^{T \times 1}$ : vecteur des rendements du marché sur les mêmes périodes ;
- $\epsilon_i \in \mathbb{R}^{T \times 1}$ : vecteur des termes résiduels supposés centrés et non corrélés avec $R_M$.

### Étape 2:  Régression des rendements moyens sur les bêtas estimés

Maintenant, avec le vecteur de $\boldsymbol{\beta}$ obtenu en faisant $N$ régressions, nous pouvons projeter les rendements moyens (l'estimateur de l'espérance) sur les bêtas et obtenir une estimation de la prime associé au facteur du marché. 

$$
\bar{R_i} = \gamma_0 + \beta_i \gamma_M + \varepsilon_i, \; \; \; \forall i \in \{1, \dots, N\} \tag{3}
$$

avec :

- $\bar{R_i}  \in \mathbb{R}$ : Rendements moyens de l'actif $i$ ;
- $\gamma_0 \in \mathbb{R}$ :Prime associé aux taux sans risque (ou aux *zero-beta security*) ;
- $\beta_i $: Sensibilité de l'actif $i$ au facteur de marché ;
- $\gamma_M \in \mathbb{R}$ : prime de risque du marché ;
- $\varepsilon_i \in \mathbb{R}$ : terme d’erreur de l'actif $i$.

Cependant, cette approche présente deux limites majeures :

-  **Incertitude sur les bêtas estimés**  
   Les séries temporelles étant souvent courtes et bruyantes, surtout pour les actifs individuels, les bêtas estimés sont peu fiables. Cela induit un biais d’atténuation entre la relation des rendements et des bêtas.

-  **Corrélation entre résidus**  
   Les actifs sont exposés à des chocs communs (macroéconomiques, sectoriels, etc.), ce qui viole l’hypothèse d’indépendance des résidus. Par conséquent, les erreurs standards sont sous-estimées, ce qui gonfle artificiellement la significativité des coefficients.


## Incertitude sur les bêtas estimés : Portefeuilles triés par bêta

Face à ces problèmes, plusieurs chercheurs, notamment Blume (1970), Friend et Blume (1970), ainsi que Black, Jensen et Scholes (1972), ont proposé d’abandonner l’analyse des actifs individuels au profit de portefeuilles.

L’idée est simple : en agrégeant plusieurs actifs, on atténue l’erreur de mesure sur les bêtas. Les portefeuilles offrent une exposition au facteur de marché plus stable, ce qui permet d’obtenir des estimations de bêta plus fiables.

Cette méthode présente un avantage important, elle permet de se concentrer sur les caractéristiques agrégées des portefeuilles, sans se préoccuper de l’identité des actifs qui les composent. En effet, un actif individuel peut voir son bêta évoluer dans le temps, mais en rebalançant périodiquement les portefeuilles, il sera naturellement réaffecté selon sa nouvelle exposition au marché.

Ainsi, ce ne sont plus les actifs qui sont évalués de façon rigide, mais plutôt des groupes dynamiques reflétant une exposition similaire au risque systématique à un moment donné.


### Méthodologie de tri

La méthode consiste à :

1. Estimer les bêtas individuels.
2. Trier les actifs par bêta croissant.
3. Former, par exemple, $p$ portefeuilles selon les percentiles.
4. Calculer le rendement moyen et le bêta moyen de chaque portefeuille.
5. Répéter périodiquement le tri pour maintenir une cohérence temporelle.

Cette procédure permet de couvrir efficacement l’éventail des bêtas, tout en maximisant la variance entre les portefeuilles. La seule différence entre les portefeuilles sont le niveau des bêtas.  

Cependant, comme le soulignent Fama et MacBeth (1973), cette méthodologie présente un biais potentiel aux extrémités de la distribution des portefeuilles. En effet, les erreurs de mesure dans l’estimation des bêtas peuvent être corrélées entre elles, ce qui entraîne une surestimation des bêtas pour les portefeuilles à haut bêta et une sous-estimation pour ceux à faible bêta.

Autrement dit, les actifs les plus extrêmes dans le classement ont tendance à être sélectionnés en raison d’une erreur de mesure plutôt que de leur véritable exposition au risque de marché. Ce phénomène peut fausser l’interprétation de la relation entre bêta et rendement, en aplatissant artificiellement la pente estimée. Nous y reviendrons !



## Corrélation entre résidus: L'importance de l'indépendance des observations en régression linéaire

En régression linéaire classique, l'indépendance des observations est une hypothèse clé pour assurer la validité des inférences statistiques. Or, dans certains contextes empiriques, comme l'estimation des primes de risque en finance, cette hypothèse peut être violée sans nécessairement biaiser les estimateurs.

Dans notre cas, les variables explicatives sont les $\beta_i$ obtenus à la première étape pour chaque actif. L’estimateur des primes de risque de l'équation (3) en notation matricielle est obtenu par :


$$
\hat\gamma = (\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top \bar R . \tag{4}
$$

Où $\hat\gamma = [\hat\gamma_0, \hat\gamma_M]$, $\boldsymbol{\beta}$ est de dimension $N \times 2$ et $\bar R$ est le vecteur de rendement moyen de dimension $N\times 1$.


Même si les observations (les actifs) ne sont pas indépendantes, cet estimateur reste **non biaisé**, à condition que les erreurs aient une espérance nulle :

$$
\begin{aligned}
E(\hat\gamma) &= E\left[(\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top \bar R\right] \\
              &= (\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top E[\bar R] \\
              &= (\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top E[\boldsymbol{\beta}\gamma + \varepsilon] \\
              &= (\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top \boldsymbol{\beta} \gamma + (\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top E[\varepsilon] \\
              &= \gamma.
\end{aligned}
$$

Cependant, le **problème survient au moment de l'inférence**. Si les observations ne sont pas indépendantes, alors la matrice de variance de l’estimateur $\hat\gamma$ devient :

$$
\begin{aligned}
\operatorname{Var}(\hat\gamma) &= \operatorname{Var}\left[(\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top \bar R\right] \\
&= (\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top \operatorname{Var}(\bar R) \left[(\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top\right]^\top \\
&= (\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top \Sigma \left[(\boldsymbol{\beta}^\top \boldsymbol{\beta})^{-1} \boldsymbol{\beta}^\top\right]^\top,
\end{aligned}
$$

où $\Sigma$ est la matrice de variance-covariance des rendements espérés. 

Le cœur du problème est donc ici de savoir comment bien estimer $\Sigma$ ? Tel que mentionné dans Cochrane (2005), le réflexe naturel en statistique serait de faire une régression des moindre carrés généralisées. Toutefois, Fama et Macbeth (1973) proposent leur procédure en 2 étapes (ormis l'étape d'estimation des bêtas). Cette procédure permet de mieux prendre en compte la variabilité temporelle et la dépendance structurelle des rendements, sans avoir à estimer directement la matrice $\Sigma$.


## La méthode Fama-MacBeth (1973)

La solution proposée par Fama-macbeth touche aux deux problèmes précédent. Premièrement, ils démontrent leur méthodologie afin d'atténuer le problème d'estimation des bêtas. Ensuite, ils proposent un modèle stochastique plus général de l'équation (1).


### Estimation des bêtas

Afin de réduire l’impact des erreurs de mesure dans l’estimation des bêtas, Fama et MacBeth suggèrent de regrouper les actifs en portefeuilles selon leur exposition estimée au risque de marché. Concrètement, les bêtas sont d’abord estimés sur une période initiale, disons de $T - k$ à $T$, puis les actifs sont triés en fonction de ces valeurs. On forme ensuite plusieurs portefeuilles, par exemple par déciles, allant des actifs les moins exposés (faibles bêtas) aux plus exposés (bêtas élevés).

L’enjeu ici est que les erreurs de mesure sur les bêtas ne sont pas aléatoires après tri. Les actifs dont les bêtas sont surévalués ont plus de chances d’être classés dans les portefeuilles de tête, et inversement pour ceux sous-évalués. Cela crée une forme de biais systématique à l’intérieur des groupes.

Pour limiter cet effet, les bêtas des portefeuilles peuvent être réestimés sur une période ultérieure, par exemple de $T$ à $T + k$. L’objectif n’est pas de corriger parfaitement les bêtas individuels, mais de lisser les erreurs de mesure à travers l’agrégation. Ainsi, les bêtas de portefeuilles, calculés comme la moyenne des bêtas de leurs composantes, sont généralement plus stables et moins bruités.

<img src="/assets/Images/Capture d’écran, le 2025-07-08 à 10.44.39.png" alt="Diagramme Fama-MacBeth" style="max-width: 100%; height: auto;">

La figure ci-dessus illustre cette logique. Chaque rectangle représente un portefeuille. Celui du haut regroupe les actifs aux bêtas estimés les plus élevés, tandis que celui du bas contient ceux aux bêtas les plus faibles. Le regroupement permet d’atténuer l’impact des erreurs individuelles ($u$) qui, en l’absence de correction, auraient tendance à biaiser les inférences statistiques.


En 1992, Shanken montre que l’erreur de mesure sur les bêtas diminue lorsque l’horizon temporel $T$ tend vers l’infini. Autrement dit, avec suffisamment de données, il devient possible d’utiliser les actifs individuels sans que l’erreur de mesure ne compromette significativement les inférences.

Toutefois, pour la suite, nous supposerons que les $\beta_i$ sont correctement estimés.


### Estimation des primes de risque

Le modèle (1) est en terme de rendement espéré. Cependant, comme nous venons tout juste de voir, estimer cette équation avec les rendements moyens posent des difficultés. L'innovation méthodologique de Fama-Macbeth se trouve dans l'équation ci-dessous,
$$
r_{i,t} = \gamma_{0,t} + \beta_i\gamma_{1,t} + \varepsilon_{i,t}. \tag{3}
$$

Où $r_{i,t}$ est le rendement de l'actif $i$ au temps $t$, $\gamma_{0,t}$ est l'ordonnée à l'origine au temps $t$, $\beta_i$ est le facteur d'exposition de l'actif $i$ au marché, $\gamma_{1,t}$ est la prime par unité de risque (*price of risk*) et $\varepsilon_{i,t}$ est l'erreur aléatoire de l'actif $i$ au temps $t$. 

Ils proposent un modèle stochastique période par période laissant varier les primes de risque aléatoirement autour du vrai paramètre sous l'hypothèse de marché efficient, c'est-à-dire, que les prix sont le reflet de toutes l'informations disponibles et qu'il est impossible de battre le marché d'une quelconque stratégie autre que l'exposition aux risques systématiques. Les prix réagissent seulement à la nouvelle information et les variations au temps $t$ sont des erreurs aléatoires de moyenne nulle. 

La méthodologie peut sembler complexe, mais elle se résume ainsi :

### Étape 1 :

- Estimer pour chaque actif $i$ les $\beta_i$ avec la régression en série temporelle suivante :

$$
R_i = \alpha_i + \beta_i R_M + \epsilon_i
$$

Où $R_i$ est le vecteur de rendement de l'actif $i$ de dimension $T \times 1$, $\alpha_i$ est la partie non expliquée par le marché pour l'actif $i$, $\beta_i$ est la sensibilité de l'actif au marché, $R_M$ est le rendement du marché et $\epsilon_i$ est l'erreur résiduelle.



### Étape 2 :

- Effectuer $T$ régressions en coupe transversale :

$$
R_t = \gamma_{0,t} + \beta\gamma_{1,t} + \varepsilon_t
$$

Où $R_t$ est un vecteur de rendement des actifs de dimension $N \times 1$, $\gamma_{0,t}$ est la prime de risque associée aux bêtas nuls, $\beta$ est le vecteur de tout les expositions des actifs calculées à l'étape 1 de dimension $N \times 1$, $\gamma_{1,t}$ est la prime de risque associée au marché au temps $t$ et $\varepsilon_t$ est l'erreur résiduelle au temps $t$. 


### Étape 3 :

- Estimation des primes de risques

$$
\begin{aligned}
\hat\gamma_{0}  = \frac{\sum^{T}\hat\gamma_{0,t}}{T}  \\
\hat\gamma_{1}  = \frac{\sum^{T}\hat\gamma_{1,t}}{T} 
\end{aligned}
$$

L'avantage de cette méthode est qu'elle permet de faire une moyenne des estimateurs non biaisés malgré la dépendance des observations et permet alors de calculer une erreur-type de cette même moyenne. En d'autres mots, nous venons de contourner le problème d'estimation de la matrice de variance covariance en effectuant $T$ régressions indépendantes et en calculant par la suite la variation des coefficients estimés dans le temps. Cette méthode s'apparente à un rééchantillonnage en évitant d’estimer directement la matrice de variance en utilisant la variation naturelle des coefficients à travers le temps.



## Des résultats empiriques qui remettent en question le modèle

En 1992, Eugene Fama et Kenneth French publient l’article The Cross-Section of Expected Stock Returns, dans lequel ils proposent un modèle empirique remettant en question les implications du CAPM. À l’époque, deux anomalies majeures restaient inexpliquées par ce dernier : l’effet de taille (size), mis en évidence par Banz (1981), et l’effet valeur (value), documenté par Basu (1983). Leur idée fut de regrouper ces deux anomalies au sein d’un seul modèle, aujourd’hui connu sous le nom de Fama-French Three-Factor Model.

Ce modèle repose sur une approche entièrement empirique, et aucune théorie économique ne permet de le dériver avec la même élégance que le CAPM. Néanmoins, le principe fondamental demeure : un portefeuille plus risqué doit, en moyenne, offrir un rendement plus élevé.

Le modèle *Fama-French Three-Factor Model* s’écrit :

$$
E[R_i] - R_f = \beta_{iM}(E[R_M] - R_f) + \beta_{iSMB}E[SMB] + \beta_{iHML}E[HML]
$$

1. **SMB (Small Minus Big)** : un facteur qui capte la surperformance moyenne des petites capitalisations par rapport aux grandes ;
2. **HML (High Minus Low)** : un facteur qui reflète la surperformance des actions à forte valeur comptable relative (valeurs) sur celles à faible B/M (croissance).


<style>
.table-fm-wrapper {
  max-width: 700px;
  margin: 2em auto;
}

.table-fm {
  width: 100%;
  border-collapse: collapse;
  font-size: 1rem;
}

.table-fm caption {
  caption-side: bottom;
  text-align: center;
  font-weight: bold;
  font-size: 0.95rem;
  padding-top: 8px;
  color: #555;
}

.table-fm th,
.table-fm td {
  border: 1px solid #ccc;
  padding: 10px 12px;
  text-align: center;
}

.table-fm thead {
  background-color: #f5f5f5;
  font-weight: bold;
}
</style>

<div class="table-fm-wrapper">
  <table class="table-fm">
    <caption>Tableau 1 — Estimation des primes de risque mensuel (Fama–MacBeth) de 1968 à 2023</caption>
    <thead>
      <tr>
        <th>Facteur</th>
        <th>Prime de risque</th>
        <th>Statistique-t</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Intercept</td>
        <td>0.0120</td>
        <td>4.93</td>
      </tr>
      <tr>
        <td>Bêta</td>
        <td>0.0005</td>
        <td>0.49</td>
      </tr>
      <tr>
        <td>Value (B/M)</td>
        <td>0.0013</td>
        <td>2.48</td>
      </tr>
      <tr>
        <td>Size (log MV)</td>
        <td>-0.0008</td>
        <td>-2.44</td>
      </tr>
    </tbody>
  </table>
</div>


Les résultats du tableau 1 indiquent que la prime de risque associée au facteur de marché (le bêta) est faible et statistiquement non significative (statistique-t de 0,49). En revanche, les facteurs liés à la taille et à la valeur sont tous deux significatifs à des niveaux conventionnels.

Autrement dit, le bêta ne semble pas constituer, à lui seul, une source de risque systématiquement récompensée. À l’inverse, les actions de petite capitalisation (valeurs faibles de log(MV)) et celles ayant un fort ratio valeur comptable / valeur de marché (B/M) affichent des primes de risque significatives, remettant ainsi en question la validité empirique du CAPM.

Le coefficient négatif associé au facteur de taille est cohérent avec l’idée que le risque supplémentaire encouru en investissant dans des entreprises de plus petite taille doit être compensé en moyenne par un rendement attendu plus élevé.

Cette formulation suggère que le risque de marché ne suffit pas à expliquer les rendements observés. En intégrant des primes de risque liées à la taille et à la valeur, le modèle offre une meilleure description des rendements moyens. Cela peut expliquer pourquoi certains portefeuilles surperforment systématiquement le marché, sans pour autant contredire l’hypothèse d’efficience, dans la mesure où ces primes sont interprétées comme des compensations pour des risques additionnels.


## Limites

L’un des arguments les plus percutants contre les tests empiriques du CAPM provient de Richard Roll (1977), qui affirme que le CAPM n’a en réalité jamais été testé et qu’il ne pourra probablement jamais l’être.

Le cœur du problème réside dans le portefeuille de marché, une composante centrale du modèle. En théorie, ce portefeuille devrait contenir l’ensemble des actifs disponibles dans l’économie, pondérés par leur valeur de marché : actions, obligations, immobilier, capital humain, actifs privés, etc. Or, en pratique, une telle mesure est inobservable. Il est impossible d’inclure tous les actifs, certains ne sont pas cotés, d’autres sont difficilement mesurables, comme le capital humain.

Par conséquent, les chercheurs se tournent vers des *proxies*, comme l'indice boursier S&P 500 par exemple, pour représenter le marché. Mais selon Roll, cette substitution change fondamentalement la nature du test : on ne teste plus le CAPM, mais plutôt la validité de l’indice utilisé comme approximation du portefeuille de marché.

Roll pousse l’argument plus loin : même si un *proxy* produit une relation linéaire entre les rendements et les bêtas, cela ne prouve en rien que cette relation découle du CAPM. Ce que l’on teste réellement, c’est si ce proxy appartient à la frontière de variance minimale, condition nécessaire mais non suffisante pour valider le modèle.

Autrement dit, tant que le véritable portefeuille de marché reste inaccessible, toute tentative de validation empirique du CAPM est fondamentalement limitée. Le rejet du modèle peut venir d’une mauvaise spécification théorique, mais aussi, et surtout, d’une approximation imparfaite de $R_M$. Roll conclut donc que l’on ne peut rien affirmer de définitif sur la validité du CAPM, car les données disponibles ne permettent pas d’isoler la performance du modèle de celle de ses hypothèses non observables.

## Données

J’ai utilisé les bases de données CRSP et Compustat disponibles via la plateforme WRDS, en suivant la procédure décrite dans [Tidy Finance – Accessing and Managing Financial Data](https://www.tidy-finance.org/r/accessing-and-managing-financial-data.html).

L’estimation des primes de risque a été effectuée selon la méthode Fama–MacBeth, telle que présentée dans [Tidy Finance – Fama-MacBeth Regressions](https://www.tidy-finance.org/r/fama-macbeth-regressions.html). Notons que l’analyse de Tidy Finance intègre également une correction pour l’autocorrélation temporelle. Cette correction n’a pas été retenue ici, car elle ne constitue pas le cœur de l’analyse exposée.

Ne disposant pas du linktable de WRDS, généralement utilisé pour effectuer une correspondance fiable entre les identifiants CRSP et Compustat, j’ai réalisé la jointure à l’aide du code CUSIP (8 caractères). Cette méthode peut introduire de légères divergences par rapport à une jointure basée sur le linktable, mais les écarts observés sont marginaux et n’affectent pas les conclusions principales.

Le code ci-dessous reproduit fidèlement l’ensemble de la procédure utilisée pour estimer les coefficients présentés dans le Tableau 1.



```r
library(tidyverse)
library(RSQLite)
library(scales)
library(slider)
library(furrr)
library(sandwich)
library(broom)

tidy_finance <- dbConnect(
  SQLite(),
  "/Your/path",
  extended_types = TRUE
)

crsp_monthly <- tbl(tidy_finance, "crsp_monthly") |>
  select(permno, cusip, date, ret_excess, mktcap) |>
  collect()

compustat <- tbl(tidy_finance, "compustat") |>
  select(datadate, cusip, be) |>
  mutate(cusip = substr(cusip,1,8))%>%
  collect()

beta <- tbl(tidy_finance, "beta_rollW_60_48") |>
  select(permno, date, beta_monthly) |>
  collect()

characteristics <- compustat |>
  mutate(date = floor_date(ymd(datadate), "month")) |>
  left_join(crsp_monthly, join_by(cusip, date)) |>          # left_join by cusip instead of gvkey
  left_join(beta, join_by(permno, date)) |>
  transmute(cusip,
            permno,
            bm = be / mktcap,
            log_mktcap = log(mktcap),
            beta = beta_monthly,
            sorting_date = date %m+% months(6)
  )

data_fama_macbeth <- crsp_monthly |>
  left_join(characteristics, join_by(permno, date == sorting_date)) |>
  group_by(permno) |>
  arrange(date) |>
  fill(c(beta, bm, log_mktcap), .direction = "down") |>
  ungroup() |>
  left_join(crsp_monthly |>
              select(permno, date, ret_excess_lead = ret_excess) |>
              mutate(date = date %m-% months(1)),
            join_by(permno, date)
  ) |>
  select(permno, date, ret_excess_lead, beta, log_mktcap, bm) |>
  drop_na()


# Cross-sectional regression

risk_premiums <- data_fama_macbeth |>
  nest(data = c(ret_excess_lead, beta, log_mktcap, bm, permno)) |>
  mutate(estimates = map(
    data,
    ~ tidy(lm(ret_excess_lead ~ beta + log_mktcap + bm, data = .x))
  )) |>
  unnest(estimates)


#Time-Series Aggregation

price_of_risk <- risk_premiums |>
  group_by(factor = term) |>
  summarize(
    risk_premium = mean(estimate),
    t_statistic = mean(estimate) / sd(estimate) * sqrt(n())
  )

```


<div id="bibliography">
  <div class="wrap">
    <ol class="bibliography">

      <li>Banz, Rolf W. (1981). <span class="title">*The Relationship Between Return and Market Value of Common Stocks.*</span> Journal of Financial Economics, 9(1), 3–18.</li>

      <li>Basu, Sanjoy. (1983). <span class="title">*The Relationship Between Earnings Yield, Market Value, and Return for NYSE Common Stocks: Further Evidence.*</span> Journal of Financial Economics, 12(1), 129–156.</li>

      <li>Black, Fischer. (1972). <span class="title">*Capital Market Equilibrium with Restricted Borrowing.*</span> Journal of Business, 45(3), 444–454.</li>

      <li>Black, Fischer, Jensen, Michael C., & Scholes, Myron. (1972). <span class="title">*The Capital Asset Pricing Model: Some Empirical Tests.*</span> In M. C. Jensen (Ed.), <span class="title">*Studies in the Theory of Capital Markets*</span> (pp. 79–121). New York: Praeger.</li>

      <li>Blume, Marshall E. (1970). <span class="title">*Portfolio Theory: A Step Towards its Practical Application.*</span> Journal of Business, 43(2), 152–174.</li>

      <li>Cochrane, John H. (2005). <span class="title">*Asset Pricing (Revised Edition).* </span> Princeton University Press.</li>

      <li>Fama, Eugene F., & MacBeth, James D. (1973). <span class="title">*Risk, Return, and Equilibrium: Empirical Tests.*</span> Journal of Political Economy, 81(3), 607–636.</li>

      <li>Friend, Irwin, & Blume, Marshall E. (1970). <span class="title">*Measurement of Portfolio Performance under Uncertainty.*</span> American Economic Review, 60(4), 607–636.</li>

      <li>Lintner, John. (1965). <span class="title">*The Valuation of Risk Assets and the Selection of Risky Investments in Stock Portfolios and Capital Budgets.*</span> The Review of Economics and Statistics, 47(1), 13–37.</li>

      <li>Markowitz, Harry. (1952). <span class="title">*Portfolio Selection.*</span> Journal of Finance, 7(1), 77–99.</li>

      <li>Mossin, Jan. (1966). <span class="title">*Equilibrium in a Capital Asset Market.*</span> Econometrica, 34(4), 768–783.</li>

      <li>Roll, Richard. (1977). <span class="title">*A Critique of the Asset Pricing Theory’s Tests. Part I: On Past and Potential Testability of the Theory.*</span> Journal of Financial Economics, 4(2), 129–176.</li>

      <li>Shanken, Jay. (1992). <span class="title">*On the Estimation of Beta Pricing Models.*</span> Review of Financial Studies, 5(1), 1–33.</li>

      <li>Sharpe, William F. (1964). <span class="title">*Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk.*</span> The Journal of Finance, 19(3), 425–442.</li>

    </ol>
  </div>
</div>
{% endkatexmm %}
