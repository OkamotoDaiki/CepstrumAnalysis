
import numpy as np

def low_cepstrum(data, index=50):
    """
    Perform cepstrum with low pass lifter. The algorithm is as follows.
        Time series data -> DFT -> abs -> log -> iDFT -> lifter -> DFT
    1. DFT the data of the 1st argument
    2. Allows audio characteristics to be separated by logarithmic spectrum.
    3. Convert to the quefrency domain by iDFT.
    4. Lifter the higher dimension by the number of index of the 2nd argument.
    5. Perform DFT and return to frequency domain
    """
    n = len(data)
    fscale = np.linspace(0, fs, n)
    dft = np.fft.fft(data, n)
    dft_abs = np.abs(dft)
    LogAmpDFT = 10*np.log10(dft_abs**2)
    cps = np.real(np.fft.ifft(LogAmpDFT))
    cpsCoef = index
    cps[cpsCoef:len(cps) - cpsCoef] = 0
    dft_cps_low = np.real(np.fft.fft(cps, n))
    return dft_cps_low, fscale


def high_cepstrum(data, index=50):
    """
    Perform cepstrum with high pass lifter. The algorithm is as follows.
        Time series data -> DFT -> abs -> log -> iDFT -> lifter -> DFT
    1. DFT the data of the 1st argument
    2. Allows audio characteristics to be separated by logarithmic spectrum.
    3. Convert to the quefrency domain by iDFT.
    4. Lifter the low dimension by the number of index of the 2nd argument.
    5. Perform DFT and return to frequency domain.
    """
    n = len(data)
    fscale = np.linspace(0, fs, n)
    dft = np.fft.fft(data, n)
    dft_abs = np.abs(dft)
    LogAmpDFT = 10*np.log10(dft_abs**2)
    cps = np.real(np.fft.ifft(LogAmpDFT))
    cpsCoef = index
    cps[:cpsCoef] = 0
    cps[len(cps) - cpsCoef:] = 0
    dft_cps_high = np.real(np.fft.fft(cps, n))
    return dft_cps_high, fscale


if __name__ == "__main__":
    """sample"""
    from FFTTool import ZeroPadding
    import matplotlib.pyplot as plt
    import soundfile

    fname = '0_jackson_0.wav' #Any wav file.
    data, fs = soundfile.read(fname)
    data = ZeroPadding(data).process()
    n = len(data)
    hamming_window = np.hamming(n)
    window_data = hamming_window*data
    dft = np.fft.fft(window_data, n)
    dft_abs = np.abs(dft)
    LogAmpDFT = 10*np.log10(dft_abs**2)
    dft_ceps_low, fscale = low_cepstrum(window_data, index=50)
    dft_ceps_high, fscale = high_cepstrum(window_data, index=50)

    plt.subplot(121)
    plt.plot(fscale[:int(fs/2)], LogAmpDFT[:int(fs/2)], color="blue")
    plt.plot(fscale[:int(fs/2)], dft_ceps_low[:int(fs/2)], color="red")
    plt.xlabel("frequency [Hz]")
    plt.ylabel("log amplitude spectrum [db]")

    plt.subplot(122)
    plt.plot(fscale[:int(fs/2)], LogAmpDFT[:int(fs/2)], color="blue")
    plt.plot(fscale[:int(fs/2)], dft_ceps_high[:int(fs/2)], color="orange")
    plt.xlabel("frequency [Hz]")
    plt.rcParams["font.size"] = 16
    plt.show()