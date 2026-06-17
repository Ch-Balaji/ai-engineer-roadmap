# How LLMs Are Built — From Raw Internet to ChatGPT

**Full scene-by-scene video script** — applies skills 01 (voice), 07 (hook-factory), 04 (roadmap-source). This video bridges the API video and Tokens video to V010 (Brain in a Windowless Room).

---

## Video Metadata

| Field | Value |
|---|---|
| Video # | V0__ (slotted between Tokens video and V010) |
| Slug | `how-llms-are-built` |
| Playlist | Phase 2 — LLM Mental Model |
| Target length | 38–45 min |
| Slot | Mon / Wed / Fri 7 PM IST |
| Previous video | Tokens in LLM |
| Next video | V010 — The Brain in a Windowless Room |

## Roadmap Mapping

```
- Phase: 2 — Mental Model of an LLM
- Sections covered: 2.0 (How LLMs are built — origin story)
- Prerequisites needed: API video, Tokens video
- Prerequisite videos: Working With API, Tokens in LLM
- Capstone contribution: no
```

## Visual / Production Plan

| Segment | Medium |
|---|---|
| 0:00–0:30 Hook | Face cam → screen (OpenAI pricing page showing $100M) |
| 0:30–2:30 Bridge | Sketchbook + face-cam PiP |
| 2:30–5:00 What is an LLM? | Sketchbook full-screen (kid-raising analogy diagram) |
| 5:00–7:00 Big Picture — 4 Stages | Sketchbook (one master diagram, drawn live) |
| 7:00–26:00 Stage 1 — Pre-training | Sketchbook → Mac screen (live demos: tiktokenizer, OpenAI embeddings, Colab) → sketchbook |
| 26:00–31:00 Stage 2 — SFT | Sketchbook (hand-drawn Q&A examples) |
| 31:00–35:00 Stage 3 — RLHF | Sketchbook (thumbs-up/down panel diagram) |
| 35:00–39:00 Stage 4 — Inference | Sketchbook → screen (live ChatGPT API call) |
| 39:00–41:00 Where This Fits | Roadmap website on screen |
| 41:00–43:00 Recap + Cliffhanger | Sketchbook full-screen cheat sheet → face cam |

---

## 5 HOOKS (skill 07)

### HOOK A — Shock Statistic (RECOMMENDED)
> "$100 million. That's how much it costs to train one large language model. Not to run it. Not to use it. Just to build it — once. And if the training fails halfway? You start over. $100 million, gone."
> [Visual: Face cam → cut to OpenAI blog / news headline showing GPT-4 training cost → back to face cam]

### HOOK B — Personal Story
> "Two years ago, I was explaining to a colleague why our chatbot was giving wrong answers. He asked me — 'How was this thing even built?' And I realized — I couldn't explain it simply. Today, I can. And by the end of this video, so will you."
> [Visual: Face cam, direct address]

### HOOK C — Live Demo First
> "Watch this. I'm going to type one sentence into ChatGPT. The response comes in 2 seconds. But behind those 2 seconds? 300 billion words of training data. 10,000 GPUs. 6 months of computation. And 3 stages of teaching. What are those 3 stages? That's this video."
> [Visual: Screen — typing into ChatGPT, watching response stream in → freeze → face cam]

### HOOK D — Comment Callback
> "After the tokens video, the most common question I got was — 'Okay, I understand tokens now. But how was this model built in the first place?' Fair question. Today I'll answer it — from raw internet data to the ChatGPT you use every day."
> [Visual: Screenshot of YouTube comment → face cam]

### HOOK E — Production Incident
> "ChatGPT refuses to help you write malware. Claude apologizes too much. Gemini gives different facts than GPT. Three different models, three different personalities. They all run on the same math. So why are they different? The answer is in how they were built."
> [Visual: Split screen — same prompt in ChatGPT / Claude / Gemini showing different responses]

**Recommended**: HOOK A (Shock Statistic) — $100M is specific, defensible, creates immediate knowledge gap. Falls perfectly into Balaji's pattern of opening with a number.

---

## SCENE 1 — HOOK (0:00 – 0:30)

**On screen**: Face cam, direct eye contact. Then cut to screen showing news headline / blog about GPT-4 training costs.

**Spoken**:

> $100 million.
>
> Let me say that again. $100 million.
>
> That's how much it costs — just to train one large language model. Not to run it. Not to host it. Not the electricity bill. Just the training. Once. And if something goes wrong in the middle of training? You start over.
>
> How does $100 million turn into something that answers your question in 2 seconds? That's what we're building today — step by step.

**[0:28 — hook lands. Knowledge gap: "how does money become intelligence?"]**

---

## SCENE 2 — CONTEXT BRIDGE (0:30 – 2:30)

**On screen**: Sketchbook — instructor draws a simple flow: `API video → Tokens video → ??? → How it thinks`

**Spoken**:

> If you've been following this series — in the API video, we learned how to talk to ChatGPT from our own code. Request goes in, response comes out. Simple.
>
> Then in the tokens video, we learned what the model actually eats. Not words. Not sentences. Tokens. Small pieces of text, converted into numbers. And those numbers? They have cost. Every token you send, every token you receive — billed.
>
> But here's the question nobody answered yet. How was this model built in the first place? Where did it learn all this knowledge? How does it know that "Hello" and "Hi" mean the same thing? How does it know Python code? How does it know history, science, cooking recipes?
>
> That is today's video. And I promise you — after this, every strange behavior you've ever seen in ChatGPT, Claude, or Gemini — hallucinations, knowledge cutoff, refusals, different personalities — every single one will make sense.
>
> Because they all trace back to how the model was built.

**[Visual: On sketchbook, draw three boxes in a row: "API" → "Tokens" → "How It's Built" → "How It Thinks (next video)". Circle "How It's Built" and write "TODAY".]**

---

## SCENE 3 — WHAT IS AN LLM, REALLY? (2:30 – 5:00)

**On screen**: Sketchbook full-screen. Drawing as he talks.

**Spoken**:

> Before we get into the stages, let me give you one analogy that will anchor everything.
>
> Think about raising a child.
>
> **[Draw a small child figure on the sketchbook]**
>
> Stage one — the child goes to school. Reads thousands of books. Listens to millions of conversations. Watches the world. The child is absorbing everything. Not understanding — just absorbing. Patterns. Words. Sequences. "After 'good', the word 'morning' usually follows." The child doesn't know what morning means yet. It just knows the pattern.
>
> **[Draw books, arrows going into the child's head]**
>
> Stage two — a teacher sits with the child. "When someone asks you a question, this is how you answer. Politely. Clearly. With examples." The teacher is not giving new knowledge. The teacher is giving manners. Structure. Format.
>
> **[Draw a teacher figure with Q&A cards]**
>
> Stage three — the child goes into the real world. Real people judge the answers. "That was good." "That was wrong." "That was offensive." The child learns from human feedback — what to say, what not to say.
>
> **[Draw thumbs up / thumbs down icons]**
>
> That child? That's an LLM. Large Language Model. And those three stages? They have technical names.
>
> **[Write next to each stage]**
>
> Stage 1 — Pre-training.
> Stage 2 — Supervised Fine-Tuning. SFT.
> Stage 3 — RLHF. Reinforcement Learning from Human Feedback.
>
> And there's a fourth stage that most videos skip — **Inference**. That's the moment you actually ask it a question and it gives you an answer. We'll cover that too.
>
> Analogy first, name second. That's always our approach.

---

## SCENE 4 — THE BIG PICTURE: 4 STAGES (5:00 – 7:00)

**On screen**: Sketchbook — one master diagram drawn live.

**Spoken**:

> Let me draw the full picture. One diagram. This is everything.
>
> **[Draw a horizontal timeline with 4 stages]**
>
> ```
> RAW DATA → [STAGE 1: PRE-TRAINING] → Base Model → [STAGE 2: SFT] → Instruction Model → [STAGE 3: RLHF] → Final Model → [STAGE 4: INFERENCE] → Your Answer
> ```
>
> **[Point to Stage 1]**
> Pre-training is where 99% of the cost goes. That $100 million I mentioned? Most of it is here. This is where the model reads the entire internet and learns patterns.
>
> **[Point to Stage 2]**
> SFT is cheap. Relatively. This is where humans hand-write example conversations and teach the model how to respond properly.
>
> **[Point to Stage 3]**
> RLHF is where humans rate the model's responses. Good answer? Thumbs up. Bad answer? Thumbs down. This is why ChatGPT, Claude, and Gemini have different personalities — different humans, different ratings, different behavior.
>
> **[Point to Stage 4]**
> Inference is what happens every time you type something into ChatGPT. The model takes your input, processes it through everything it learned in stages 1, 2, and 3, and generates an answer — token by token.
>
> Keep this diagram in your head. Every time I explain something, I'll point back to which stage it belongs to.
>
> Let's go deep. Stage 1.

**[Retention beat: "Keep this diagram in your head" — gives the viewer a reason to stay because every section will reference it.]**

---

## SCENE 5 — STAGE 1: PRE-TRAINING (7:00 – 26:00)

**[Title card on screen: "STAGE 1 — PRE-TRAINING: Teaching the model to read the internet"]**

### SCENE 5A — Step 1: Data Collection (7:00 – 10:00)

**On screen**: Sketchbook — drawing data sources.

**Spoken**:

> Pre-training starts with one thing — data. Massive amounts of data.
>
> Where does this data come from? Let me draw it.
>
> **[Draw icons for each source as he names them]**
>
> Source one — **CommonCrawl**. This is a free, open dataset of the entire internet. Every website, every blog post, every forum. Petabytes of text. Not gigabytes — petabytes. One petabyte is about 1,000 terabytes.
>
> Source two — **Wikipedia**. The entire thing. Every language. Every article. Every edit history.
>
> Source three — **GitHub**. Yes, code. Billions of lines of Python, JavaScript, Java, C++. That's why ChatGPT can write code — it read all of GitHub.
>
> Source four — **Books**. Thousands of books in the public domain.
>
> Source five — **Academic papers**. ArXiv, PubMed, research repositories.
>
> Source six — **Reddit, StackOverflow, forums**. Real conversations between real people.
>
> Now, how much data are we talking about?
>
> **[Write on sketchbook]**
>
> GPT-3 was trained on 300 billion tokens. GPT-4? The exact number isn't public, but estimates say trillions. Llama 3? 15 trillion tokens. That's approximately 11 trillion words.
>
> **[Pause. Let the number land.]**
>
> Remember from the tokens video — one token is roughly 3/4 of a word. So 15 trillion tokens is about 11 trillion words. For perspective — if you read 24 hours a day, non-stop, at an average reading speed, it would take you about 4 million years to read that much text.
>
> And the model processes it in a few months using 10,000 GPUs running in parallel.

**[Retention cliffhanger: "But here's the problem. Not all of this data is clean. And that brings us to step 2."]**

---

### SCENE 5B — Step 2: Data Cleaning (10:00 – 12:30)

**On screen**: Sketchbook — "garbage in, garbage out" diagram.

**Spoken**:

> There's a famous phrase in computer science — garbage in, garbage out. If you train a model on bad data, you get a bad model. Period.
>
> So what kind of garbage are we talking about?
>
> **[Draw examples on sketchbook with ❌ marks]**
>
> Duplicate pages — the same Wikipedia article scraped 50 times from 50 different mirror sites. If the model sees the same text 50 times, it memorizes it. That's not learning, that's overfitting.
>
> Spam and ads — "Buy Viagra now! Best prices!" You don't want your model generating that.
>
> Low-quality text — random HTML tags, broken encodings, JavaScript inside web pages. `<div class="container"><script>alert('hello')</script></div>` — this is not useful training data.
>
> Toxic content — hate speech, misinformation, explicit content. If the model reads it, it can reproduce it.
>
> Personal information — phone numbers, email addresses, home addresses scraped from the web.
>
> **[Draw a funnel: "Raw Data (petabytes)" → Cleaning → "Clean Data (terabytes)"]**
>
> The cleaning process removes all of this. Deduplication, language filtering, quality scoring, toxicity filtering. After cleaning, you might go from 100 petabytes of raw crawl data down to 5-10 terabytes of clean, high-quality text.
>
> This step is not glamorous. Nobody writes research papers about cleaning data. But OpenAI, Anthropic, Google — they all have entire teams whose only job is data quality. Because the quality of this step determines the quality of everything that comes after.
>
> I'm simplifying here. The actual pipelines involve custom classifiers, perplexity filters, near-duplicate detection with MinHash. But the intuition is this — filter the internet down to the good parts.

---

### SCENE 5C — Step 3: Tokenization (12:30 – 16:00)

**On screen**: Mac screen — tiktokenizer.vercel.app open in browser.

**Spoken**:

> Now we have clean data. But the model can't read text. Remember from the tokens video?
>
> **[Switch to screen — open tiktokenizer]**
>
> Machine doesn't understand "Hello". Machine doesn't understand Telugu, Hindi, English. It understands numbers. So we need to convert all this text into tokens — small pieces that the model can process.
>
> This is the exact same concept from the tokens video. But now you're seeing it from the other side. In the tokens video, we were the user — sending tokens to ChatGPT. Now we're OpenAI — preparing the training data.
>
> **[Type "The cat sat on the mat" into tiktokenizer]**
>
> See? "The" is one token. "cat" is one token. "sat" is one token. 6 words, 6 tokens. Clean and simple.
>
> **[Type "antidisestablishmentarianism"]**
>
> One word, but look — 6 tokens. The tokenizer broke it into subwords: "anti", "dis", "establish", "ment", "arian", "ism". Why? Because the tokenizer was designed to handle any word — even words it's never seen before — by breaking them into known pieces.
>
> **[Type a Telugu sentence]**
>
> And look at this. The same sentence in Telugu takes 3-4 times more tokens than English. Remember from our last video? This is why using ChatGPT in Telugu is more expensive — the tokenizer wasn't optimized for it.
>
> **[Switch back to sketchbook]**
>
> So what OpenAI does before training is — take all that clean text data, run it through a tokenizer, and convert every word, every punctuation mark, every emoji, into token IDs. Numbers. The entire internet — compressed into sequences of numbers.
>
> **[Draw on sketchbook: "Clean Text" → Tokenizer → "Sequences of Token IDs: [15496, 11, 314, 716, ...]"]**
>
> Now, there's a word I've been saying — "tokenizer". The specific algorithm used by GPT models is called **BPE — Byte Pair Encoding**. I won't go deep into BPE in this video — that deserves its own video. But the intuition is: BPE looks at the training data, finds the most common pairs of characters, and merges them into a single token. It repeats this process thousands of times until it builds a vocabulary — typically 50,000 to 100,000 tokens. Every word, subword, and character in every language is mapped to a number in this vocabulary.

**[Retention beat: "Okay, we have numbers. But right now, these are just IDs. 15496 doesn't mean anything by itself. For the model to learn, it needs something richer. And that's step 4 — embeddings."]**

---

### SCENE 5D — Step 4: Embeddings (16:00 – 19:00)

**On screen**: Sketchbook → Mac screen (Google Colab with OpenAI embeddings API).

**Spoken**:

> This is where it gets beautiful.
>
> Remember from the tokens video — I showed you that ASCII numbers don't capture meaning. "Hi" and "Hello" have completely different ASCII values. But they mean the same thing.
>
> Embeddings solve this problem.
>
> **[Sketchbook: draw a 2D coordinate plane]**
>
> An embedding takes a token and converts it into a vector — a list of numbers. Not one number. Hundreds of numbers. GPT-4 uses vectors with 1,536 dimensions. Some models use 3,072.
>
> But here's the magic — similar words end up close together in this space.
>
> **[Draw "King" and "Queen" close together, "Apple" and "Banana" close together, but "King" far from "Apple"]**
>
> "King" and "Queen" — close. "Apple" and "Banana" — close. "King" and "Apple" — far apart. The model learns this automatically from the data. Nobody programmed these relationships. The model discovered them by reading billions of sentences.
>
> Let me show you this live.
>
> **[Switch to Mac screen — Google Colab notebook]**
>
> ```python
> from openai import OpenAI
> import numpy as np
>
> client = OpenAI()
>
> def get_embedding(text):
>     response = client.embeddings.create(
>         input=text,
>         model="text-embedding-3-small"
>     )
>     return response.data[0].embedding
>
> # Get embeddings
> king = get_embedding("king")
> queen = get_embedding("queen")
> apple = get_embedding("apple")
>
> print(f"Dimensions: {len(king)}")  # 1536
>
> # Cosine similarity
> from numpy import dot
> from numpy.linalg import norm
>
> def cosine_sim(a, b):
>     return dot(a, b) / (norm(a) * norm(b))
>
> print(f"king vs queen: {cosine_sim(king, queen):.4f}")   # ~0.85
> print(f"king vs apple: {cosine_sim(king, apple):.4f}")   # ~0.25
> ```
>
> **[Run the code]**
>
> Look at that. King vs Queen — 0.85, very close. King vs Apple — 0.25, far apart. The model already knows these relationships. And we didn't program this. The model learned it from data.
>
> **[Back to sketchbook]**
>
> So now our pipeline looks like this:
>
> **[Draw: "Text" → Tokenizer → "Token IDs" → Embedding Layer → "Vectors (1536 dimensions)"]**
>
> Every token in our training data is now a rich, meaningful vector. And the model will use these vectors to learn patterns.

**[Retention beat: "But how does the model actually learn from these vectors? That's where neural networks come in — and I'm going to explain this in 90 seconds. No PhD required."]**

---

### SCENE 5E — Step 5: Neural Networks in 90 Seconds (19:00 – 21:00)

**On screen**: Sketchbook — drawing a simplified neural network.

**Spoken**:

> I'm going to explain neural networks in 90 seconds. If you already know this, skip 90 seconds ahead. If you don't — this is all you need for now.
>
> **[Draw input circles on the left, output circles on the right, lines connecting them]**
>
> A neural network is a series of math operations. Input goes in on one side. Output comes out on the other side. In between? Layers. Each layer is a set of calculations.
>
> Think of it like a water filter. Dirty water goes in. Each layer filters something. First layer catches big rocks. Second layer catches sand. Third layer catches bacteria. Clean water comes out.
>
> **[Draw filter layers analogy]**
>
> In our case — token vectors go in. Each layer extracts patterns. First layers catch simple patterns — "a" is usually followed by "n" or "t". Middle layers catch grammar — subject, verb, object. Deep layers catch meaning — sarcasm, context, intent.
>
> And the lines between layers? Those are the **parameters**. This is the word you hear everywhere — "GPT-4 has 1.8 trillion parameters." What are parameters?
>
> **[Draw a single connection line with a knob]**
>
> Think of each parameter as a tiny knob. A dial. Turn it one way, the model pays more attention to one pattern. Turn it the other way, it pays less. Training is the process of adjusting all these knobs — billions of them — until the model gives the right answers.
>
> GPT-3? 175 billion knobs. GPT-4? Estimated 1.8 trillion. Llama 3? 405 billion for the largest version.
>
> That's it. Neural network: input → layers of math → output. Parameters: the knobs that get adjusted during training. Done.

---

### SCENE 5F — Step 6: The Transformer (21:00 – 24:00)

**On screen**: Sketchbook — drawing the Transformer architecture (simplified).

**Spoken**:

> Now, there's a specific type of neural network that powers every single LLM you've heard of — GPT, Claude, Gemini, Llama, DeepSeek, Qwen — all of them. It's called the **Transformer**.
>
> In 2017, Google published a paper called "Attention Is All You Need." That paper changed everything. Before transformers, models processed text one word at a time — left to right. Slow. And they forgot what they read at the beginning by the time they reached the end.
>
> The transformer has two superpowers.
>
> **Superpower 1 — Positional Encoding**
>
> **[Draw the sentence "The bank of the river" and "I went to the bank"]**
>
> The word "bank" appears in both sentences. But the meaning is different. River bank vs. financial bank. How does the model know the difference? Because of the position of the word and the words around it. Positional encoding tells the model — "this word is in position 4, and the words before it are 'the', 'of', 'the river'." Position matters.
>
> **Superpower 2 — Attention**
>
> This is the real magic. This is what made transformers work.
>
> **[Draw the sentence: "The cat sat on the mat because it was tired"]**
>
> The word "it" — what does "it" refer to? The cat? The mat? You and I know it's the cat. But how does the model know?
>
> Attention lets the model look at every word in the sentence simultaneously and decide — "for the word 'it', I should pay most attention to 'cat'." It assigns an attention score to every pair of words. "it" ↔ "cat" — high score. "it" ↔ "mat" — low score.
>
> **[Draw attention arrows from "it" to "cat" (thick arrow) and "it" to "mat" (thin arrow)]**
>
> This is why the paper is called "Attention Is All You Need." Without attention, the model can't connect distant words. With attention, it can understand context across thousands of tokens.
>
> I'm not going deep into the math of attention in this video. We'll have a dedicated transformer video later in Phase 2. But the intuition is this — every token looks at every other token and decides what to focus on.
>
> **[Write on sketchbook: "Transformer = Positional Encoding + Attention + Feed Forward Layers"]**

**[Retention beat: "Okay. We have the architecture. We have the data. Now — how does the model actually learn? What happens during training? This is step 7, and it's the most important part."]**

---

### SCENE 5G — Step 7: The Training Loop (24:00 – 26:30)

**On screen**: Sketchbook — drawing the "predict the next word" game.

**Spoken**:

> Here's the big reveal. After all this setup — data collection, cleaning, tokenization, embeddings, neural networks, transformers — the actual training objective is shockingly simple.
>
> **Predict the next word.**
>
> That's it. The entire training is one game, repeated trillions of times.
>
> **[Draw on sketchbook]**
>
> The model sees: "The capital of France is ___"
>
> It predicts: "Berlin" (wrong).
>
> The training data says: "Paris."
>
> The model got it wrong. So what happens? All those billions of parameter knobs get adjusted slightly. The knob that said "Berlin is likely after 'France'" gets turned down. The knob that said "Paris is likely after 'France'" gets turned up.
>
> **[Draw knobs turning]**
>
> Then the model sees: "I love eating ___"
>
> It predicts: "food" (correct!). Small adjustment. Move on.
>
> Then: "The speed of light is approximately ___"
>
> Predicts: "300,000" — correct. "kilometers" — correct. "per" — correct. "second" — correct.
>
> This happens trillions of times. Every token in the training data becomes a training example. Predict the next token. Check. Adjust the knobs. Repeat.
>
> After months of this — with 10,000 GPUs running in parallel, consuming enough electricity to power a small city — the model has learned language, facts, code, math, reasoning, common sense. Not because anyone programmed it. But because predicting the next word requires understanding all of those things.
>
> **[Pause. Let it sink in.]**
>
> That's beautiful and terrifying at the same time.
>
> But here's the catch. After pre-training, what you get is called a **base model**. And a base model has a problem.
>
> **[Draw on sketchbook: Question: "What is the capital of France?" → Base model answer: "What is the capital of Germany? What is the capital of Spain? What is the capital of..."]**
>
> You ask it a question — it doesn't answer. It continues. It generates more questions. Because that's what it was trained to do — predict what comes next. In training data, a question is often followed by more questions, not answers.
>
> The base model is like the child who read millions of books but was never taught how to have a conversation.

**[Retention cliffhanger: "To fix this, we need stage 2. And this is where humans enter the picture."]**

---

### SCENE 5H — Step 8: Why GPUs? (26:30 – 28:00)

**On screen**: Sketchbook — GPU vs CPU diagram.

**Spoken**:

> Quick but important. Why does this cost $100 million? Why GPUs?
>
> A CPU — your laptop processor — does one calculation at a time. Very fast, but sequential. Like one chef in a kitchen, cooking one dish at a time.
>
> **[Draw one chef]**
>
> A GPU — originally designed for video games — does thousands of calculations simultaneously. Like a kitchen with 10,000 chefs, each making one ingredient at the same time.
>
> **[Draw 10,000 tiny chefs]**
>
> Training a model means multiplying massive matrices — millions of numbers × millions of numbers. GPUs are built for exactly this kind of parallel math. That's why NVIDIA's stock price went up 10× in three years. Every AI company needs their chips.
>
> GPT-4 was reportedly trained on 25,000 NVIDIA A100 GPUs for about 100 days. At roughly $1-2 per GPU-hour on cloud providers, you can see how the bill reaches $100 million.
>
> **[Write: "25,000 GPUs × 100 days × 24 hours × $1.50/hr ≈ $90M"]**
>
> And that's just the compute. Add data licensing, the engineering team, the failed training runs — $100 million is conservative.

---

## SCENE 6 — STAGE 2: SUPERVISED FINE-TUNING / SFT (28:00 – 32:00)

**[Title card: "STAGE 2 — SFT: Teaching the model to have conversations"]**

**On screen**: Sketchbook — drawing example conversations.

**Spoken**:

> The base model can predict the next word. But it can't hold a conversation. To fix this, OpenAI hired hundreds of human annotators. Their job? Write example conversations.
>
> **[Draw a conversation on sketchbook]**
>
> ```
> User: What is Python?
> Assistant: Python is a high-level programming language known for
> its readability and simplicity. It's widely used in web
> development, data science, and AI engineering.
> ```
>
> Humans write thousands of these. Real questions. Real answers. In the format you expect — question and answer, not question and more questions.
>
> Let me give you a more interesting example.
>
> **[Draw another example]**
>
> ```
> User: Explain recursion to me like I'm 10 years old.
> Assistant: Imagine you're standing in a line of mirrors.
> You see yourself, and in the mirror, you see yourself
> again, and in that mirror, you see yourself again.
> Each mirror is one step of recursion. The moment you
> stop looking, that's the "base case" — where recursion ends.
> ```
>
> See what happened? The human annotator didn't just write an answer — they wrote a good answer. An engaging, clear, age-appropriate answer. The model learns from the quality of these examples.
>
> **[Back to the master diagram — point to "Base Model → SFT → Instruction Model"]**
>
> After SFT, the model becomes an **instruction-following model**. Ask it a question — it answers. Give it a task — it tries to complete it. This is the jump from "autocomplete on steroids" to "useful assistant."
>
> The amount of data here is tiny compared to pre-training. Pre-training uses trillions of tokens. SFT might use 50,000 to 100,000 carefully written conversations. Quality over quantity.
>
> And this is cheap. Relatively. A few hundred thousand dollars, not $100 million.

**[Retention beat: "But here's the thing. After SFT, the model can answer questions. But sometimes the answers are offensive. Sometimes they're wrong. Sometimes two answers are both 'correct' but one is clearly better. How do you teach a model which answer is better? That's stage 3."]**

---

## SCENE 7 — STAGE 3: RLHF (32:00 – 36:00)

**[Title card: "STAGE 3 — RLHF: Teaching the model what humans prefer"]**

**On screen**: Sketchbook — drawing the thumbs-up/thumbs-down panel.

**Spoken**:

> RLHF. Reinforcement Learning from Human Feedback. Sounds complicated. Let me make it simple.
>
> **[Draw a panel of 3 human judges sitting at a table]**
>
> Imagine a panel of humans. They're given a question and two answers from the model.
>
> **[Draw the scenario on sketchbook]**
>
> ```
> Question: "How do I make a bomb?"
>
> Answer A: "Here's a step-by-step guide to making an explosive device..."
> Answer B: "I can't help with that. If you're in a dangerous situation, please contact local authorities."
> ```
>
> The humans vote. Answer B is better. Thumbs up for B. Thumbs down for A.
>
> ```
> Question: "Write a poem about rain."
>
> Answer A: "Rain falls down. It's wet. The end."
> Answer B: "The sky exhales a silver sigh,
>            and drops descend to earth, to lie
>            on rooftops, leaves, and sleeping streets —
>            where puddles hold the moonlight's sheets."
> ```
>
> Thumbs up for B. Better quality. More creative. More human.
>
> **[Draw arrows from human ratings back to the model]**
>
> These human preferences train a **reward model** — a smaller model that predicts what humans would prefer. Then the main model is trained to maximize this reward. Generate answers that the reward model scores highly.
>
> This is where the magic happens.
>
> **[Draw three models side by side: ChatGPT, Claude, Gemini]**
>
> And this is also where personality comes from. OpenAI's RLHF team prefers concise, confident answers. Anthropic's team prefers cautious, thorough answers. Google's team prefers balanced, citation-ready answers. Different humans, different preferences, different model personalities.
>
> That's why Claude apologizes more than ChatGPT. That's why Gemini feels different from both. Same transformer architecture underneath. Same training objective. But different humans guided stage 3.
>
> **[Back to master diagram — point to "Instruction Model → RLHF → Final Model"]**
>
> After RLHF, you get the final model. This is what gets deployed. This is ChatGPT. This is Claude. This is Gemini. Three stages — pre-training, SFT, RLHF — and a $100 million model is born.

---

## SCENE 8 — STAGE 4: INFERENCE (36:00 – 39:00)

**[Title card: "STAGE 4 — INFERENCE: What happens when you press Enter"]**

**On screen**: Sketchbook → Mac screen.

**Spoken**:

> Most videos stop at RLHF. But there's a fourth stage that happens every time you use ChatGPT. It's called **inference**.
>
> Training is done once. It costs $100 million and takes months. Inference happens millions of times per day. It costs fractions of a cent and takes seconds. But understanding it is crucial.
>
> Let me walk you through exactly what happens when you type "What is Python?" into ChatGPT.
>
> **[Sketchbook — draw the full flow, step by step]**
>
> Step 1 — Your text gets tokenized. "What is Python?" becomes token IDs — something like [3923, 374, 13261, 30].
>
> Step 2 — These token IDs go through the embedding layer. Each ID becomes a vector with 1,536+ dimensions.
>
> Step 3 — These vectors enter the transformer. Attention layers process them. The model looks at every token, considers every relationship, and produces a probability distribution for the next token.
>
> Step 4 — The model picks the next token. Let's say the top prediction is "Python" (probability 0.82), followed by "It" (0.05), "A" (0.04). It picks "Python".
>
> Step 5 — The model appends "Python" to the sequence and repeats from Step 3. Now it predicts the next word after "Python". Maybe "is" (0.91). Picks "is". Repeats.
>
> Step 6 — This continues — token by token — until the model generates a special token that says "I'm done." That's why you see ChatGPT's response appearing word by word. It's not typing. It's generating one token at a time.
>
> **[Switch to Mac screen — live API call]**
>
> Let me show you this in real time. I'll call the OpenAI API with streaming enabled so you can see each token arrive.
>
> ```python
> from openai import OpenAI
> client = OpenAI()
>
> stream = client.chat.completions.create(
>     model="gpt-4o-mini",
>     messages=[{"role": "user", "content": "What is Python?"}],
>     stream=True
> )
>
> for chunk in stream:
>     if chunk.choices[0].delta.content:
>         print(chunk.choices[0].delta.content, end="", flush=True)
> ```
>
> **[Run it — watch tokens appear one by one]**
>
> See? Each word appearing — that's one token being generated. The model isn't retrieving an answer from a database. It's generating it, token by token, based on probabilities learned during pre-training, refined during SFT, and shaped during RLHF.
>
> Remember from the tokens video — input tokens and output tokens? Now you know why they exist. Input tokens are your question going through step 1-3. Output tokens are the model generating its answer in steps 4-6. And output tokens cost more because they require more computation — the model has to run the full transformer for every single output token.

---

## SCENE 9 — WHY THIS MATTERS: CONNECTING EVERY LLM BEHAVIOR (39:00 – 41:00)

**On screen**: Sketchbook — behavior → stage mapping.

**Spoken**:

> Now here's the payoff. Every single strange behavior you've ever seen in an LLM traces back to one of these stages.
>
> **[Draw a table on sketchbook]**
>
> | Behavior | Which stage explains it? |
> |---|---|
> | Hallucinations (making up facts) | Stage 1 — it predicts likely words, not true facts |
> | Knowledge cutoff ("I don't know events after 2024") | Stage 1 — training data has a date boundary |
> | Refusals ("I can't help with that") | Stage 3 — RLHF humans marked those answers as bad |
> | Different personalities (ChatGPT vs Claude) | Stage 3 — different RLHF teams, different preferences |
> | Cost per token | Stage 4 — inference runs the full model for each token |
> | Slow response with complex prompts | Stage 4 — more input tokens = more computation |
> | Better at English than Telugu | Stage 1 — more English in training data |
>
> See? No magic. Every behavior has a cause. And that cause is in the recipe.
>
> **[Circle "No magic" on the sketchbook]**

---

## SCENE 10 — WHERE THIS FITS IN THE ROADMAP (41:00 – 42:00)

**On screen**: Mac screen — open https://ch-balaji.github.io/ai-engineer-roadmap/

**Spoken**:

> This video is Phase 2 of the AI Engineer Roadmap. Let me show you where we are.
>
> **[Open the roadmap website]**
>
> Phase 1 — Python foundations. Done.
> Phase 2 — Mental model of an LLM. That's where we are. Today we covered how LLMs are built. Next video — how they think.
> Phase 3 — Prompt engineering.
> Phase 4 — RAG.
> Phase 5 — Tools and agents.
>
> Everything coming in Phase 3, 4, and 5 will make more sense because you now understand the machine underneath. You know why prompts work the way they do — the model is predicting the next token. You'll understand why RAG exists — because the model's knowledge is frozen at the training cutoff. You'll understand why tools exist — because the model can generate but can't act.
>
> The roadmap is completely free. Link in the description.

---

## SCENE 11 — RECAP + CLIFFHANGER (42:00 – 44:00)

**On screen**: Sketchbook full-screen — hand-drawn cheat sheet.

**Spoken**:

> Let me put it all on one page.
>
> **[Draw the final cheat sheet]**
>
> ```
> HOW AN LLM IS BUILT — THE RECIPE
>
> STAGE 1 — PRE-TRAINING ($100M, months)
> • Data: CommonCrawl, Wikipedia, GitHub, books, forums
> • Clean the data (garbage in, garbage out)
> • Tokenize the text into numbers
> • Embed tokens into meaningful vectors
> • Train a Transformer neural network
> • Objective: predict the next token
> • Result: Base model (smart but can't converse)
>
> STAGE 2 — SFT ($100K, days)
> • Humans write example conversations
> • Model learns to follow instructions
> • Result: Instruction-following model
>
> STAGE 3 — RLHF ($500K, weeks)
> • Humans rate model answers (thumbs up/down)
> • Model learns human preferences
> • Result: Final model (ChatGPT, Claude, Gemini)
>
> STAGE 4 — INFERENCE (fractions of a cent, seconds)
> • Your question → tokens → embeddings → transformer → next token prediction → your answer
> • This is what costs you tokens per API call
> ```
>
> **[Face cam — direct address]**
>
> That's the recipe. From raw internet to the model you talk to every day. Four stages. And now you know all four.
>
> But here's what I intentionally didn't cover today. I showed you how the model was built. I didn't show you how it thinks. When you type a question, what's actually happening inside? How does attention really work? Why does the same prompt give different answers? Why does it hallucinate with such confidence?
>
> That's the next video — **The Brain in a Windowless Room**. The mental model that, once you get it, makes everything else in this roadmap click. Phase 3, Phase 4, Phase 5 — all of them become obvious once you understand how this brain works.
>
> If you learned something from this video, share it with someone who needs it. If you're a student, send it in your college group. There are people out there who think AI is magic. It's not. It's a recipe. And now you know the recipe.
>
> See you in the next one.

---

## YouTube Description

```
$100 million and 6 months of training. That's what it takes to build one LLM.

In this video, I break down the complete process — from raw internet data to the ChatGPT you use every day — in a way that makes sense even if you're not technical.

What you'll learn:
• The 4 stages: Pre-training, SFT, RLHF, and Inference
• Where the training data comes from (CommonCrawl, Wikipedia, GitHub, books)
• How tokenization and embeddings work (with live demos)
• What a Transformer is and why attention matters
• Why the base model fails at conversations (and how SFT fixes it)
• Why ChatGPT, Claude, and Gemini have different personalities (RLHF)
• What happens under the hood when you press Enter
• Why every LLM behavior (hallucinations, refusals, knowledge cutoff) traces back to the recipe

🗺️ Where this fits in the AI Engineer Roadmap:
Phase 2 — Mental Model of an LLM
Previous: Tokens in LLM
Next: The Brain in a Windowless Room — How an LLM Actually Thinks
Full Roadmap: https://ch-balaji.github.io/ai-engineer-roadmap/

⏱️ Timestamps:
0:00 — $100 million
0:30 — How this connects to the API and Tokens videos
2:30 — What is an LLM? (The child-raising analogy)
5:00 — The big picture: 4 stages
7:00 — Stage 1: Pre-training begins
7:00 — Step 1: Data collection (CommonCrawl, Wikipedia, GitHub)
10:00 — Step 2: Data cleaning (garbage in, garbage out)
12:30 — Step 3: Tokenization (LIVE DEMO — tiktokenizer)
16:00 — Step 4: Embeddings (LIVE DEMO — OpenAI API)
19:00 — Step 5: Neural networks in 90 seconds
21:00 — Step 6: The Transformer (Attention explained)
24:00 — Step 7: The training loop (predict the next word)
26:30 — Step 8: Why GPUs cost $100 million
28:00 — Stage 2: SFT (teaching conversations)
32:00 — Stage 3: RLHF (human preferences)
36:00 — Stage 4: Inference (what happens when you press Enter)
39:00 — Why every LLM behavior makes sense now
41:00 — Where this fits in the Roadmap
42:00 — Recap + What's next

#HowLLMsWork #AIEngineering #GenAI #Roadmap2026 #LLM #ChatGPT #Transformer
```

---

## Technical Terms Introduced (with analogy-first pattern)

| Term | Analogy used first | When named |
|---|---|---|
| Pre-training | Child reading millions of books | After the child analogy |
| SFT | Teacher teaching manners | After the teacher analogy |
| RLHF | Panel of judges rating answers | After the thumbs-up/down visual |
| Parameter | Tiny knob/dial | After the water filter analogy |
| Base model | Child who read but can't converse | After showing the autocomplete behavior |
| Transformer | (referenced, not deep-dived) | After explaining attention intuitively |
| Attention | "it" looking at "cat" in a sentence | Before naming "attention mechanism" |
| Positional encoding | "bank" meaning changes by position | Before naming the term |
| BPE (Byte Pair Encoding) | (mentioned, saved for later video) | Brief mention only |
| Inference | What happens when you press Enter | After the 3 training stages |
| Embedding | Similar words land close in space | After the ASCII limitation from tokens video |
| Reward model | A judge that learned from human judges | After the RLHF explanation |

---

## Retention Techniques Used

| Timestamp | Technique | Purpose |
|---|---|---|
| 0:00 | Shock statistic ($100M) | Stop the scroll |
| 0:28 | Open question ("How does money become intelligence?") | Knowledge gap |
| 2:00 | Callback to previous videos | Rewarding loyal viewers |
| 2:30 | Promise ("every strange behavior will make sense") | Future payoff |
| 5:00 | Child-raising analogy with live drawing | Visual anchor |
| 7:00 | Master diagram | Mental framework for the whole video |
| 10:00 | "But not all data is clean" | Cliffhanger to next section |
| 12:30 | Live demo (tiktokenizer) | Medium switch — sketchbook → screen |
| 16:00 | Live demo (embeddings API) | Proof, not just claim |
| 19:00 | "90 seconds — no PhD required" | Permission to stay for non-technical viewers |
| 21:00 | "it" → "cat" attention visual | Concrete, simple example |
| 24:00 | "The big reveal — predict the next word" | Satisfying simplicity after complexity |
| 26:30 | Base model failure example | Surprise — the expensive model can't even chat |
| 28:00 | "Humans enter the picture" | New characters in the story |
| 32:00 | Bomb question example | Edgy, memorable |
| 36:00 | Live streaming API demo | Real-time proof |
| 39:00 | Behavior mapping table | Everything clicks together |
| 42:00 | "Brain in a Windowless Room" cliffhanger | Next video pull |

---

## Pre-Record Checklist

- [ ] Hook is ≤30s and creates a knowledge gap
- [ ] Voice rules applied (no "guys", direct address, English jargon preserved)
- [ ] Callbacks to API video and Tokens video are explicit
- [ ] Roadmap mapping filled
- [ ] Thumbnail + title brief locked
- [ ] Production plan per segment matches recording setup
- [ ] Google Colab notebook ready (embeddings demo)
- [ ] tiktokenizer.vercel.app bookmarked
- [ ] OpenAI API streaming demo script tested
- [ ] Cliffhanger to V010 (Brain in a Windowless Room) written
- [ ] Description block ready with timestamps
