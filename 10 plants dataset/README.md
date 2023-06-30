# Dataset Rootpath
This is where you should save your dataset.
The image data of `10 plants dataset` itself is not included in this repository, feel free to use your own dataset instead.

The data structure of your dataset should be like:

```
.
├── test
│   ├── 0.jpg
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
├── test_labels.json
├── train
│   ├── class A
│   │   ├── 0.jpg
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   └── ...
│   └── class B
│       ├── 0.jpg
│       ├── 1.jpg
│       ├── 2.jpg
│       └── ...
└── val
    ├── class A
    │   ├── 0.jpg
    │   ├── 1.jpg
    │   ├── 2.jpg
    │   └── ...
    └── class B
        ├── 0.jpg
        ├── 1.jpg
        ├── 2.jpg
        └── ...
```
You should organize your test labels according to `test_labels.json`.
