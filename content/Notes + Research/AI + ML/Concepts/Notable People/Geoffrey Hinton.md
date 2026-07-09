---
title: Geoffrey Hinton
tags:
  - ai/ml
  - notable_people
  - concept
draft:
created: 2025-06-17

modified: 2025-07-05

published: 2025-06-17

---
![[Pasted image 20250617175820.png|400]]

Considered by many as the "Godfather of AI," viewed as a leading figure in the deep learning community. Announced his resignation from Google in 2023 to be able to "freely speak out about the risks of A.I."

In 2018, he along with [[Yann LeCun]] and [[Yoshua Bengio]] won the [ACM A.M. Turing Award](https://en.wikipedia.org/wiki/Turing_Award) for their foundational work on [[Deep Learning]]. They are sometimes referred to as the "Godfathers of AI."

---
## Interviews
- [What Leaders Need to Understand About AI with Nobel Laureate Geoffrey Hinton](https://www.youtube.com/watch?v=32f9MgnLSn4)
## Quotes
#### Why did Dr. Hinton seemingly change his mind about the dangers of AI? 
> [!quote]- It was because of the research I was doing at Google. 
> Okay, I was trying to figure out whether you could design analog large language models that would use much less power and I began to fully realize the advantage of being digital. So all the models we've got at present are digital, and if you're a digital model you can have exactly the same neural network with the same weights in it running on several different pieces of hardware, like thousands of different pieces of hardware. 
> 
> And then you can get one piece of hardware to look at one bit of the internet and another piece of hardware to look at another bit of the internet. And each piece of hardware can say how would I like to change my internal parameters (my weights) so I can absorb the information I just saw. And each of these separate pieces of hardware can do that and then they can just average all the changes to the weights because they're all using the same weights in exactly the same way and so averaging makes sense. You and I can't do that. 
> 
> And if they've got a trillion weights, they're sharing information at like a trillions of bits, every time they do this averaging. Now you and I, when I want to get some knowledge from my head into your head, I can't just take the strength of the connections between neurons and average them with the strength of the connections between your neurons because our neurons are different. We're analog and we're just very different brains, so the only way I have getting knowledge to you is I do some actions and if you trust me you try and change the connection strengths in your brain so that you might do the same things. 
> 
> And if you ask well how efficient is that? Well if I give you a sentence, it's only a few hundred bits of information at most, so it's very slow. We communicate just a few bits per second. These large language models running on digital systems can communicate trillions of bits a second, so **they're billions of times better than us at sharing information.** That got me scared, right? 
> 
> I was thinking if we want to use much less power we should think about whether it's possible to do this analog, and because you can use much less power you can also be much sloppier in the design of the system. Because what's going to happen is you don't have to manufacture a system that does precisely what you tell it to which is what a computer is. You can manufacture a system with a lot of slop in it, and it will learn to use that sloppy system. Which is what our brains are.
> 
> [Source](https://www.youtube.com/watch?v=mvAeKSBTD8c)



