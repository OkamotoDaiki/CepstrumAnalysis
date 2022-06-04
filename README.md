# Cepstrum Analysis

This program that uses the lifter of cepstrum analysis to separate spectral envelopes and small fluctuation components.
 
# DEMO
 
The following logarithmic amplitude spectrum can be obtained by using the sample program.
*The blue graph is the log amplitude spectrum of the sample sound source.
*The red graph is the spectrum envelope by cepstrum analysis.
*The orange graph is a fine variation component by cepstrum analysis.

![Graph](https://github.com/OkamotoDaiki/CepstrumAnalysis/issues/1#issue-1260662158)

# Features
 
The spectrum envelope can be obtained with low_cepstrum(), and the fine fluctuation component can be obtained with high_cepstrum(). In addition, the number of dimensions of quefrency can be specified by the index of the 2nd argument.
 
# Requirement
 
* Python 3.8.10
* numpy 1.21.4
 
# Installation

You can import it with the following program.

```python
import CepstrumAnalyis
import soundfile
data = soundfile.read(fname)
dft_cps_low = CepstrumAnalysis.low_cepstrum(data, index=50)
```
 
# Usage
 
Refer to the sample program.
 
# Author
* Oka.D.
* okamotoschool2018@gmail.com