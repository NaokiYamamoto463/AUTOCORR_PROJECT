import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def read_bin_as_bits(path):
    data = np.fromfile(path, dtype=np.uint8)
    bits = np.unpackbits(data)
    return bits.astype(np.float64)

def autocorrelation(x, max_lag):
    x_mean = np.mean(x)
    denom = np.sum((x - x_mean) ** 2)

    result = []

    for h in range(max_lag + 1):
        if h == 0:
            r = 1.0
        else:
            numerator = np.sum(
                (x[:-h] - x_mean) * (x[h:] - x_mean)
            )
            r = numerator / denom

        result.append(r)

    return np.array(result)

def main():
    input_file = list(Path("data").glob("*.bin"))

    if len(bin_files := list(Path("data").glob("*.bin"))) == 0:
        print("dataフォルダに .bin ファイルが見つかりませんでした。")
        return
    
    input_file = bin_files[0]
    max_lag = 100

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    bits = read_bin_as_bits(input_file)
    ac = autocorrelation(bits, max_lag)

    np.savetxt(output_dir / "autocorrelation.csv", ac, delimiter=",")

    lags = np.arange(len(ac))

    diff = np.diff(ac)

    peak_lags = [0]
    peak_values = [ac[0]]

    for i in range(1, len(diff)):
        if diff[i - 1] > 0 and diff[i] < 0:
            peak_lags.append(i)
            peak_values.append(ac[i])

    plt.figure()
    plt.plot(lags, ac, label="Autocorrelation")

    plt.scatter(peak_lags, peak_values, color="red", zorder=5, label="Peaks")
    plt.plot(peak_lags, peak_values, color="red", linestyle="--", label="Peak line")

    plt.xlabel("Lag h")
    plt.ylabel("Autocorrelation r(h)")
    plt.title("Autocorrelation Function")
    plt.grid(True)
    plt.legend()
    plt.savefig(output_dir / "autocorrelation.png")

    print(f"input file: {input_file}")
    print(f"bits: {len(bits)}")
    print("saved: output/autocorrelation.csv")
    print("saved: output/autocorrelation.png")

if __name__ == "__main__":
    main()
