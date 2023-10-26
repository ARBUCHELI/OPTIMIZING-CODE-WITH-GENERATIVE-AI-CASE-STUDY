class StatisticsCalculator:
    @staticmethod
    def calculate_mean_and_variance(data):
        n = len(data)
        if n == 0:
            return None, None

        mean = 0
        M2 = 0
        for x in data:
            delta = x - mean
            mean += delta / n
            delta2 = x - mean
            M2 += delta * delta2

        if n < 2:
            variance = 0
        else:
            variance = M2 / (n - 1)

        return mean, variance

    @staticmethod
    def calculate_median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            middle1 = n // 2
            middle2 = middle1 - 1
            median = (sorted_data[middle1] + sorted_data[middle2]) / 2
        else:
            median = sorted_data[n // 2]
        return median

# Example usage:
data = [1, 2, 3, 4, 5]

mean, variance = StatisticsCalculator.calculate_mean_and_variance(data)
standard_deviation = (variance ** 0.5)
median = StatisticsCalculator.calculate_median(data)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
print("Median:", median)