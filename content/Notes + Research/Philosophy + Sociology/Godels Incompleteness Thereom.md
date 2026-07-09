---
title: Godels Incompleteness Thereom
draft: 
tags:
  - thought
created: 2025-06-28

modified: 2025-06-28

published: 2025-06-28

---
TL;DR: Within axiomatic systems, `TRUE` statements can be `provable` or `unprovable`. 

Before this, mathematicians thought that anything `TRUE` had to be `provable`. Ever since the ancient greeks, we believed that any true statement in math had a proof. 

BUT there might be conjectures that are true (Goldbachs Conjecture) in mathematics, even if there is no proof.

>[!note] Liars Paradox
>`This statement is false`
>This is an example of the Liar Paradox. It's self-referential and leads to a contradiction. 
>If the statement is assumed to be true, then it must be false. But if it's assumed to be false, then it must be true as it claims. 
>This leads to a paradox, or an infinite loop. 
>
>Verbal paradoxes are fine since, you don't expect sentences to have inherit truth in them. BUT in mathematics, all statements are known to be either `TRUE` or `FALSE`

---

Godel created the **Godel Coding System** which could turn any mathematical statement into a number. So any axioms could be turned into a code number. 
And every code number could be worked back into a statement. Just like how computers turn text into ASCII numbers. 

With his system, he could start to talk about mathematics using mathematics itself. So now you can use this system to figure out if a particular statement is provable from mathematical axioms

If Godel coded a statement that expresses itself to be `unprovable` mathematically, then is it either `TRUE` or `FALSE` in his Coding System?

First let's assume it's `FALSE` -> This means this statement is actually `provable`. But in mathematics, this is impossible since a `provable` statement must be `TRUE`. So we started with something we assumed was `FALSE`, and came to the conclusion that it is `TRUE` which is inconsistent. 

SO this means the statement can't be false, since that would be a mathematical contradiction. 

This means the statement has to be `TRUE` -> A mathematical equation must be either true or false. Which means this `TRUE` statement is claiming it is `unprovable`.

SO Godel showed that you can have a `TRUE` statement which cannot be `provable` within the system of mathematics. 

This basically leads to an infinite regress problem, since you can continue to add axioms that are `TRUE` but `unprovable` to mathematics, thus you can never really prove mathematics as a completely `provable` and consistent system.

---
From [Wikipedia](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems#Relationship_with_computability):
>The first incompleteness theorem states that no [consistent system](https://en.wikipedia.org/wiki/Consistency "Consistency") of [axioms](https://en.wikipedia.org/wiki/Axiom "Axiom") whose theorems can be listed by an [effective procedure](https://en.wikipedia.org/wiki/Effective_procedure "Effective procedure") (i.e. an [algorithm](https://en.wikipedia.org/wiki/Algorithm "Algorithm")) is capable of [proving](https://en.wikipedia.org/wiki/Mathematical_proof "Mathematical proof") all truths about the arithmetic of [natural numbers](https://en.wikipedia.org/wiki/Natural_number "Natural number"). For any such consistent formal system, there will always be statements about natural numbers that are true, but that are unprovable within the system.

>The second incompleteness theorem, an extension of the first, shows that the system cannot demonstrate its own consistency.