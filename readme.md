# Python API for llama.cpp

I found many llama.cpp python wrapper, **none** of them really works, so I have to build my own.

The purpose for building python bridge for llama.cpp mainly was:

- llama.cpp provides a fast implementation on CPU (GPU requires too much mem), while still get a resonable speed;
- some situation I really need python (build my own chatbot server), it was currently based on a python base software foundation;
- python helps you integrated with many advanced applications more quickly.


I might bridge it into rust in the future as well.


> still work in progress, but you can star and fork subscribe my updates.


## Install

Run:

```
pip install -e .
```


## API Design

this wrapper using pybind, os basically I have redesign the previous c++ API. to make it more pythonic, I also provide a class called `HumbleLLaMas` for engage with c++.

```
from llamapy.llama import HumbleLLaMas


llamabot = HumbleLLaMas()
# you can call LLaMa, Alpaca, Vicuna, Chinese-Vicuna at ease (with different tokenizer possible)
```

Above APIs still under design.




