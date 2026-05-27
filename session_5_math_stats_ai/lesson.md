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

This became very real in 2012. Geoffrey Hinton and two of his PhD students at Toronto built AlexNet — a neural network trained almost entirely on matrix operations — and crushed the ImageNet competition. Google immediately recognised what had happened and acquired the team for around $44 million. Three years later, Google Brain open-sourced TensorFlow, the very framework they used internally to train their own models. That decision put the same tools Google used in-house into the hands of every researcher and student on the planet. Facebook's AI lab (FAIR) followed in 2016 with PyTorch — a more Pythonic alternative that researchers found easier to experiment with. Today PyTorch is the dominant framework for training new models, including most of the frontier LLMs. Meta open-sourced it and it became the industry standard.

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

There is a famous example of these ideas at scale. In 2006, Netflix offered $1 million to whoever could improve their recommendation algorithm by 10%. The winning team's solution was built on matrix factorisation — representing each user and each film as a vector, and using dot products to predict which films a user would enjoy. The same linear algebra from the section above. The winning entry took three years of work from the best teams in the world. That xG model we're building uses the same statistical foundations as every recommendation system in production today — Netflix, Spotify, YouTube.

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

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** What is the dot product of the vectors [2, 3] and [4, 1]?
- A) [8, 3]
- B) 11 ✓
- C) 14
- D) [6, 4]

**Q2.** In gradient descent, what does the derivative of the loss function tell you?
- A) The exact minimum of the loss
- B) The total error of the model
- C) The slope at the current point — which direction to adjust the parameter ✓
- D) The learning rate to use

**Q3.** A goalkeeper saves 70% of penalties. He just saved two in a row. What is the probability he saves the next penalty?
- A) More than 70% — he's in good form
- B) Less than 70% — a goal is "due"
- C) Exactly 70% ✓
- D) Cannot be determined

**Q4.** In the player stats vector `Mbappe = [27, 8, 142, 203, 18.3]`, what does the xG value of 18.3 represent, and why might a manager care that his actual goals (27) are much higher than his xG?

**Q5.** What does a correlation of −0.9 between two variables tell you? Give a football example of two stats that might be negatively correlated.

**Q6.** What is the loss function in machine learning, and what value are we trying to reach through training?
- A) A measure of the model's speed; we want it as large as possible
- B) A measure of how wrong a prediction is; we want it as close to zero as possible ✓
- C) The learning rate; we want it equal to 1
- D) The dot product of weights and inputs; we want it positive

**Q7.** Explain in your own words how a neural network "learns." Use the gradient descent metaphor from this session.

**Q8 (explain in your own words).** xG (Expected Goals) is described as a logistic regression model. Based on what you learned about probability and ML in this session, explain what inputs such a model might use and what its output represents.

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — (2×4) + (3×1) = 8 + 3 = 11. The dot product multiplies matching elements and sums the results.

**Q2.** C — The derivative tells us the slope at the current point. A positive slope means move left (decrease the parameter); a negative slope means move right (increase it). This is how the "ball rolls downhill."

**Q3.** C — Each penalty is an independent event. Past outcomes do not change the probability of future ones. The 70% save rate remains unchanged regardless of what happened before.

**Q4.** xG of 18.3 means the model expected him to score about 18 goals based on shot quality; scoring 27 means he is significantly outperforming his xG, suggesting elite finishing ability — or he may be on an unsustainable run of luck that could regress.

**Q5.** A correlation of −0.9 means the two variables move strongly in opposite directions. Football example: the number of goals conceded per game and a team's league position — teams that concede more tend to finish lower in the table.

**Q6.** B — The loss function measures prediction error. Gradient descent adjusts model parameters step by step to reduce this error toward zero (or as close as possible).

**Q7.** Model answer: A neural network starts with random weights (guesses). It makes a prediction, measures how wrong it was using the loss function, then uses gradient descent to figure out which direction to adjust each weight to reduce the error. This is repeated thousands of times — like a ball rolling downhill toward the lowest point, each step making predictions slightly more accurate.

**Q8.** Model answer: An xG model takes inputs about a shot — distance from goal, angle to goal, whether it was a header or a foot shot, whether it came from open play or a set piece. The output is a probability between 0 and 1 representing the chance that shot results in a goal (e.g., 0.23 = 23% chance). It was trained on thousands of historical shots where we know the outcome, and the model learned which combinations of inputs tend to produce goals.

---

## 📚 Research Materials

> 💡 **Start here:** Watch "But what is a neural network?" by 3Blue1Brown (https://www.youtube.com/watch?v=aircAruvnKk) — it is the single best visual explanation of how neural networks work as matrix operations, and it directly brings together vectors, dot products, and gradient descent from this session.

### 🎬 Films & Documentaries

| Title | Year | What to Watch For |
|-------|------|-------------------|
| *AlphaGo* | 2017 | DeepMind's documentary about the Go-playing AI; shows gradient descent and neural network training in practice through the lens of a real competition — the loss curves from this session are what drove every move |
| *iHuman* | 2019 | Norwegian documentary on AI's societal impact; opens with the mathematical foundations (vectors, probability) and connects them to the systems shaping daily life |
| *Moneyball* | 2011 | The xG-equivalent concept applied to baseball; every model discussed (OBP, player value metrics) is a regression model using the same statistical ideas from this session |

### 📺 YouTube

| Video / Channel | Link | Why Watch |
|-----------------|------|-----------|
| "But what is a neural network?" — 3Blue1Brown | https://www.youtube.com/watch?v=aircAruvnKk | The definitive visual explanation of neural networks as matrix multiplication; Part 1 of a 4-part series |
| "Gradient Descent, How Neural Networks Learn" — 3Blue1Brown | https://www.youtube.com/watch?v=IHZwWFHWa-w | Part 2 of the same series; animates gradient descent exactly as described in this session |
| "The Mathematics of Machine Learning" — Zach Star | https://www.youtube.com/watch?v=Rt6beTKDtqY | Connects linear algebra, calculus, and probability to ML — mirrors this session's structure |
| "Bayes Theorem Explained" — 3Blue1Brown | https://www.youtube.com/watch?v=HZGCoVF3YvM | Visual proof of Bayes' theorem using area diagrams — makes the formula intuitive |
| "Expected Goals Explained" — Tifo Football | https://www.youtube.com/watch?v=zSWhMnFOsvc | Football analytics journalists explain xG for a general audience — exactly the model built in this session |
| "Andrew Ng on AI" — Stanford HAI | https://www.youtube.com/watch?v=21EiKfQYZXc | Lecture-style talk by one of the key people from this session on the state and direction of AI |

### 📖 Books

| Title | Author | Level | Covers | Free |
|-------|--------|-------|--------|------|
| *The Art of Statistics* | David Spiegelhalter | Easy | Readable introduction to statistical thinking; covers distributions, correlation, and probability using real-world examples including sport | — |
| *Mathematics for Machine Learning* | Deisenroth, Faisal & Ong | Medium | Free PDF online; covers linear algebra, calculus, and probability specifically as they apply to ML — the mathematical backbone of this session | [Free →](https://mml-book.github.io/) |
| *Neural Networks and Deep Learning* | Michael Nielsen | Medium | Free online book; builds neural networks from scratch using gradient descent; the most approachable deep-learning text | [Free →](http://neuralnetworksanddeeplearning.com) |
| *The Signal and the Noise* | Nate Silver | Easy–Medium | How probabilistic thinking works in sport, politics, and science; Silver's xG-equivalent work for baseball is woven throughout | — |
| *Deep Learning* | Goodfellow, Bengio & Courville | Hard | The graduate-level textbook of the field written by two of the key people from this session; free online at deeplearningbook.org | [Free →](http://deeplearningbook.org) |

### 🌐 Articles & Interactive Resources

| Resource | URL | What It Covers |
|----------|-----|----------------|
| "Neural Networks" — 3Blue1Brown (video series) | https://www.3blue1brown.com/topics/neural-networks | Full 4-part series with supplemental explanations — the visual companion to this session |
| StatsBomb Open Data | https://github.com/statsbomb/open-data | Real shot data you can use to build the xG model from this session; includes distance, angle, and outcome |
| Distill.pub — Interactive ML Explanations | https://distill.pub | Research articles with interactive visualisations of gradient descent, neural networks, and attention mechanisms |
| Khan Academy — Statistics and Probability | https://www.khanacademy.org/math/statistics-probability | Free course reinforcing mean, variance, correlation, and normal distributions from this session |
| Playground.tensorflow.org | https://playground.tensorflow.org | Interactive neural network in the browser — drag layers, watch gradient descent converge, no code required |

### 🔗 People to Look Up

- **Geoffrey Hinton** — "Godfather of Deep Learning"; pioneered backpropagation and deep neural networks at the University of Toronto; awarded the 2024 Nobel Prize in Physics for his work on artificial neural networks.
- **Yann LeCun** — Chief AI Scientist at Meta; invented convolutional neural networks (CNNs) in the 1990s; CNNs power every computer vision system including those that track players in football.
- **Yoshua Bengio** — Université de Montréal professor; co-winner of the 2018 Turing Award with Hinton and LeCun for deep learning; research focuses on the probabilistic foundations of neural networks.
- **Andrew Ng** — Co-founder of Google Brain; created the deep learning specialisation on Coursera taken by millions of engineers; made the gradient descent and neural network concepts from this session universally accessible.
- **Nate Silver** — Statistician and founder of FiveThirtyEight; brought Bayesian probability and regression modelling to mainstream sports and political analysis; his work on baseball xG-equivalents inspired football analytics.
