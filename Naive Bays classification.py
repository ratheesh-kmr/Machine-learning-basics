# Given probabilities
P_C = 0.008  # Probability of having cancer
P_not_C = 1 - P_C  # Probability of not having cancer
P_T_given_C = 0.98  # Probability of positive test given cancer
P_T_given_not_C = 0.03  # Probability of positive test given no cancer

# Part (a) - First test is positive
# Calculate P(T) - total probability of a positive test
P_T = P_T_given_C * P_C + P_T_given_not_C * P_not_C

# Calculate P(C|T) - posterior probability of cancer given a positive test
P_C_given_T = (P_T_given_C * P_C) / P_T

print(f"Posterior probability of having cancer after first positive test: {P_C_given_T:.5f}")

# Part (b) - Second test is positive (independent)
# For the second test, we use the posterior P(C|T) from the first test as the new prior
P_T_second_given_C = 0.98  # Probability of positive result in the second test given cancer
P_T_second_given_not_C = 0.03  # Probability of positive result in the second test given no cancer

# Update P(T|C) for the second test
P_T_second = P_T_second_given_C * P_C_given_T + P_T_second_given_not_C * (1 - P_C_given_T)

# Calculate P(C|T_second) - posterior probability after second positive test
P_C_given_T_second = (P_T_second_given_C * P_C_given_T) / P_T_second

print(f"Posterior probability of having cancer after second positive test: {P_C_given_T_second:.5f}")
