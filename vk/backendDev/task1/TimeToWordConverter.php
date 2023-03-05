<?php

class TimeToWordConverter implements TimeToWordConvertingInterface
{
    public function convert(int $hours, int $minutes): string
    {
        $hourWords = [
            1 => 'час', 2 => 'два', 3 => 'три', 4 => 'четыре',
            5 => 'пять', 6 => 'шесть', 7 => 'семь', 8 => 'восемь',
            9 => 'девять', 10 => 'десять', 11 => 'одиннадцать',
            12 => 'двенадцать'
        ];

        $minuteWords = [
            1 => 'одна', 2 => 'две', 3 => 'три', 4 => 'четыре',
            5 => 'пять', 6 => 'шесть', 7 => 'семь', 8 => 'восемь',
            9 => 'девять', 10 => 'десять', 11 => 'одиннадцать',
            12 => 'двенадцать', 13 => 'тринадцать', 14 => 'четырнадцать',
            15 => 'пятнадцать', 16 => 'шестнадцать', 17 => 'семнадцать',
            18 => 'восемнадцать', 19 => 'девятнадцать', 20 => 'двадцать',
            30 => 'тридцать', 40 => 'сорок', 50 => 'пятьдесят'
        ];

        if ($minutes === 0)
        {
            return $hourWords[$hours] . " часов";
        }
        elseif ($minutes === 15)
        {
            return "четверть " . $hourWords[$hours + 1];
        }
        elseif ($minutes === 30)
        {
            return "половина " . $hourWords[$hours + 1];
        }
        elseif ($minutes === 45)
        {
            return "без пятнадцати " . $hourWords[$hours + 1];
        }
        elseif ($minutes === 59)
        {
            return "без одной " . $hourWords[$hours + 1];
        }
        elseif ($minutes < 21 || $minutes === 30)
        {
            return $minuteWords[$minutes] . " минут " . ($minutes < 21 ? 'после' : '') . " " . $hourWords[$hours];
        }
        else
        {
            $minuteWordsFirst = $minuteWords[$minutes - ($minutes % 10)];
            $minuteWordsLast = $minuteWords[$minutes % 10];
            return $minuteWordsFirst . " " . $minuteWordsLast . " минут после " . $hourWords[$hours];
        }
    }
}