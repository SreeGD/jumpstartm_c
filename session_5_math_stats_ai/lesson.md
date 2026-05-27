# Session 5 — The Math Engine Behind AI
## Fundamentals of Maths and Stats for AI

**Duration:** 2–3 hours  
**the teacher's prep:** Have the xG scatter plot ready to run live. Prepare shot data CSV or hardcode it.

---

## 🎯 Goal

By the end of this session, Student understands:
- How linear algebra (vectors, matrices) powers neural networks
- What gradient descent is and how it's connected to derivatives
- How probability and statistics underpin AI decisions
- That xG (Expected Goals) is a real ML model he can understand

---

## 📖 the teacher's Narrative

### Hook

*"Netflix knows you'll watch that show before you do. Spotify built your playlist from 30 seconds of listening history. Every time you search Google, 500 models run in parallel. All of them — every single one — reduce to three topics from your 12th-grade textbook: calculus, linear algebra, and probability."*

---

### Linear Algebra — Neural Networks Are Matrix Math

*"A neural network is just a series of matrix multiplications. That's the whole secret."*

**Vectors** — a list of numbers. In AI: a player's stats vector.
```
Mbappe = [27, 8, 142, 203, 18.3]
          goals assists dribbles carries xG
```

**Matrix** — a grid of numbers. In AI: the "weights" — what the network learned.

**Dot product** — multiply matching elements and sum:
```
[1, 2, 3] · [4, 5, 6] = 1×4 + 2×5 + 3×6 = 32
```

*"The dot product is how a neural network combines input features with weights. Every layer of a neural network is: output = matrix × input + bias."*

Connect to 12th grade: Student knows vectors from physics. He knows matrix multiplication. *"You already know how neural networks work at the mathematical level."*

---

### Calculus — Gradient Descent is Just Finding the Minimum

*"How does a neural network learn? It makes a prediction, measures how wrong it was, then adjusts. Gradient descent is the adjustment mechanism — and it's just derivatives."*

**The key idea:** If we have a function that measures "wrongness" (called the loss function), we want to find the minimum — where wrongness is lowest. The derivative tells us which direction is downhill.

```
loss = (prediction - truth)²

If derivative > 0 → we're on the upward slope → move left (decrease parameter)
If derivative < 0 → we're on the downward slope → move right (increase parameter)
```

*"Think of it as a ball rolling downhill. The derivative is the slope. The ball always rolls toward the bottom."*

**Show the animation:** Run the xG lab live. Plot the loss going down with each step.

*"This is exactly what ChatGPT's training did — except the 'ball' was rolling through a landscape with 175 billion dimensions."*

---

### Probability & Statistics — How AI Decides

**Distributions:** Data has patterns. Heights follow a bell curve (normal distribution). Goals per game follow a Poisson distribution. Stock returns roughly follow a normal distribution.

*"When an AI predicts something, it's not giving you one answer — it's giving you a probability distribution. 'This shot has a 23% chance of going in.' That's probability, not certainty."*

**Bayes' Theorem** — updating beliefs with evidence:
```
P(A|B) = P(B|A) × P(A) / P(B)
```

Sports example: *"A striker scores 25% of shots on target. He's had 3 shots on target this match with no goals. What's the probability he scores on his next shot on target?"*  
Still 25%. Each shot is independent. Past failures don't reduce future probability.  
*"This is why pundits who say 'he's due a goal' are wrong. Bayes says otherwise."*

**Key stats in AI/sports:**
- Mean, variance, standard deviation — measure centre and spread of data
- Correlation — how two variables move together (goals and xG should be highly correlated)
- Regression — fitting a line through data to predict

---

## ⚡ Wow Moment

Run the xG scatter plot live. Then ask:

*"If you drew a smooth S-curve through this data, you'd have a logistic regression model — the xG model that Premier League clubs pay £100k for. You just built the intuition from scratch."*

Then show: StatsBomb's published xG model documentation. It uses the same inputs — distance, angle, shot type — that they're plotting. Real clubs pay for this. Student understands it.

---

## 🔑 Key Concepts Checklist

- [ ] Vector — a list of numbers, represents a data point or direction
- [ ] Dot product — element-wise multiply and sum; core of neural networks
- [ ] Matrix multiplication — transforming vectors; what each neural network layer does
- [ ] Loss function — measures how wrong a prediction is
- [ ] Gradient descent — adjusting parameters by following the slope of the loss
- [ ] Derivative — tells you the slope at a point; which direction is downhill
- [ ] Normal distribution — bell curve; mean ± standard deviation
- [ ] Correlation — how two variables relate (−1 to +1)
- [ ] Probability — AI outputs are probability distributions, not certainties
- [ ] xG — Expected Goals; a logistic regression model on shot data

---

## Teaching Notes for Teacher

- Start with linear algebra through player stats vectors — Student can relate to these numbers.
- The gradient descent explanation with the "ball rolling downhill" is the key metaphor. Make it visual — draw it.
- Don't derive Bayes' Theorem. Just show the intuition — probabilities update with evidence.
- The lab is the centrepiece of this session. Run it slowly. Explain every line.
- Great question: *"If gradient descent finds the minimum, how does it know it's not stuck in a local minimum?"* (Spoiler: it often is. This is a real problem. Random restarts, momentum, and learning rate schedules help.)
