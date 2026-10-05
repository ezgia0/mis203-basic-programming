# Week 3 Lab: Order Approval Policy

## Boundary Tests (Sınır Testleri Tablosu)
| Order Amount | Available Stock | Requested Quantity | Is Member | Expected Result |

| 499.99 TRY | 10 | 2 | yes | Approved, Standard pricing applied. Final price: 499.99 TRY |
| 500.00 TRY | 10 | 2 | yes | Approved, Member discount of 10% applied. Final price: 450.00 TRY |
| 501.00 TRY | 10 | 2 | yes | Approved, Member discount of 10% applied. Final price: 450.90 TRY |

## Testing Notes
* **One test I ran:** I tested a scenario where the requested quantity (15) was greater than the available stock (10). The program correctly rejected the order and did not show a final price.
* **One thing I changed after testing:** Initially, I only checked if the requested quantity was greater than the stock. After testing, I realized users could enter `0` or negative numbers, so I changed the condition to `requested_quantity <= 0 or requested_quantity > available_stock` to prevent invalid zero or negative orders.
*
