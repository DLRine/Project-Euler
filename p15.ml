let rec mult n = if n <= 1 then 1 else n*(mult  (n-1))
let r = (mult 40)/((mult 20) * (mult 20))