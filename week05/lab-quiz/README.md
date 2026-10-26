# Week 5 Lab: Reusable Shipping Quote

## Test I ran
I tested the discount threshold: `discount_rate(999)` returns `0` and `discount_rate(1000)` returns `0.10`.

## What I changed after testing
At first I wrote `amount > 1000`, so an order of exactly 1000 TL got no discount and the assert failed. I changed it to `amount >= 1000`.

## print vs return
`print` only shows a value on the screen. `return` sends the value back to the caller, so it can be stored, used in another function or checked with `assert`.
