# german-political-parties-image-classification

Classifying images of images posted on Twitter by German political parties with an accuracy of ~ 83.5%.

## 0. Setup

1.  install [Pipenv](https://github.com/pypa/pipenv/)
2.  `pipenv install`
3.  install [fastai](http://docs.fast.ai/#Installation)
4.  `pipenv shell`

## 1. get all tweets

```
python get_twitter_images.py
```

## 2. split into folders

```
split_folders imgs --fixed 200 200 --oversample
```

## 3. Train

See the notebook.
