#!/bin/sh

f_test() {
  #statements
  a=$1
  echo $a
  true
}

echo 1
f_test 3
./test.py
