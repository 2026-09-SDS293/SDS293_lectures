library(tidyverse)
data <- data_frame(ID = c(1,2,3,4), color = c("b", "b", "r", "g"), values = c(1, 1, 1, 1))

data
data |>
  pivot_wider(names_from = color, values_from = values)