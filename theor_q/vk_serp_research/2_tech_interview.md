# (Второе) Большое (2-ч часовое) техническое собеседование

> План от hr

* будете решать задачку (лайвкодинг) Попишете на плюсах и питоне.  
* Поспрашивают по алгоритмам и структурам данных. 
* МЛ: базовая математика, классический МЛ, логистическая регрессия, градиентный бусинг,  DL/NLP


## Ответы 

###  Лайв кодинг

* python: Прошло 4 дня после, как прошел АА секцию в ya

* c++ нужно повторить и записать ключевые вопросы/ответы



### Алгосики и структуры данных 

* 

### МЛ: базовая математика
* Градиент - это вектор частных производных 
* Градиенты частых многомерных функций [Тык](https://education.yandex.ru/handbook/ml/article/matrichnoe-differencirovanie)
    * 1 
    * 2
* Backpropogation - эффективный подсчет производных. Правило дифференцирования сложной функции.

$$f(x) = g_m(g_{m - 1}(...(g_1(x))...))$$
$$\frac{\partial f}{\partial x} = \frac{\partial g_m}{\partial g_{m - 1}} \frac{\partial g_{m - 1}}{\partial g_{m - 2}} ... \frac{\partial g_{2}}{\partial g_1} \frac{\partial g_1}{\partial x}$$

Прямым проходом считаем значения узлов, далее посчитать градиент в узле и подставить значение функции и перемножить. 

[Для чего skip-connection - не только же для борьбы с затуханием градиента?](https://habr.com/ru/articles/688350/) - попытка избавиться от лишних симметрий в параметрическом множестве [много локальных минимумом по пути будет]



* Антиградиет указвывает направление наискорейшего роста функции (анти - соответвенно наиско уменьшения)






### Классический МЛ
Есть основные задачи: 
* Регрессии 
* Классификации 
* Класстеризации


**Регрессии** - предсказываем линейной функцией число. $y(x) = w^T x$. Веса подбираются минимизируя ошибку (MSE <- loss func, MAE, MAPE). 


[Если завести вероятностную модель $y(x) = w^T x + \varepsilon, \varepsilon \thicksim  N(0, \sigma^2), y \thicksim N(w^T x, \sigma^2)$ распределния наших данных от "истинной модели" - то максимизируюя правдоподобие получается минимизация того же MSE.](https://education.yandex.ru/handbook/ml/article/veroyatnostnyj-podhod-v-ml)


$P(y| x, w) = \prod_i P(y_i| x_i, w) \thicksim e^{-\frac{(y_i - w^T x_i)^2}{2 \sigma^2}}$

### Логистическая регрессия
[так же тута](https://education.yandex.ru/handbook/ml/article/veroyatnostnyj-podhod-v-ml)

Хотим предсказывать не любое число из $[-\infty, \infty]$, а из $[0, 1]$ применим $sigmoid(x) = \frac{1}{1 + e^{-x}}$,  $\sigma(-x) = 1 - \sigma(x), монотонна$


Минимизируем кросс энтропию $\sum_i y_i \ln \hat{y_i}$ - лосс появляется, если заведем вероятностную модель, где $y_i | x_i \thicksim Bern(\sigma(<x, w>))$ [для многоклассовой softmax]

Если максимизировать правдоподобие, нужно минимизировать кросс-энтропию


### Градиентный бусинг

> введение, независимое обьединение 
* Дерево
* Бэггинг, Случайный лес

> [бустинг,  последователньое обьединение, GBDT](https://education.yandex.ru/handbook/ml/article/gradientnyj-busting)

Есть функция ошибки $L(y, x) = MSE(y, a(x)) -> min$

будем строить $a_k(x) = b_1(x) + b_2(x) + .. + b_k(x)$

Тобишь каждый следующий алгоритм предсказывает ошибку предыдущего [при MSE совпадает с антиградиентом лосса!] 

На каждом шагу текущая компонента учиться предсказывать антиградиент ошибки предыдущего алгоритма


[9.1. Bias-variance decomposition
](https://education.yandex.ru/handbook/ml/article/bias-variance-decomposition)

###  DL/NLP
>  DL
* Линейные слои
* Функции активации
* Реглизации: batchnorm, dropout
* skip connection
* Convalution neural network: pulling, stride, padding ... 
* RNN, LSTM, (GRM ?)
* [TRANSFORMER](https://habr.com/ru/articles/781770/) 
    * encoder + decoder
    * self attention(Q, K, V) = $softmax(\frac{Q K^T}{\sqrt{d}} ) V$
    * multi attention
    * Feed fording 
    * DECODER: masking

    * Обогощение одной и той же последовательности
* [BERT](https://habr.com/ru/companies/otus/articles/702838/): только ENCODER -  закрываем слова масочками и угадываем их. 

Про оптимизаторы не забывть: до Adam

> NLP, [тык, tf-idf](https://habr.com/ru/companies/otus/articles/755772/)

* токенизация [какие бывают]
* даление стоп-слов
* лемматизация 
* нормализация текста

tf-idf:
term-freq(t, d)
Inverse Document Frequency(t)

TF-IDF(t, d) = TF(t, d) * IDF(t)

word2vec, glove


