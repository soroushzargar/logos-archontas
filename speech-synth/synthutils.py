# Used for reading, resampling and writing audio data
import librosa
# Used for array manipulation
import numpy as np


class noisyDataGenerator:
    @staticmethod
    def generateNoisySignal(cleanSignal, noiseSignal, cleanSr,
                            noiseSr, SNR, verbos):
        # Check whether the clean and noise signal have same sample rate
        if cleanSr != noiseSr:
            resampledNoiseSignal = librosa.core.resample(
                noiseSr, noiseSr, cleanSr
            )
            noiseSignal = resampledNoiseSignal

        # Reshaping noise to be equal to clean signal in length
        if cleanSignal.shape[0] > resampledNoiseSignal.shape[0]:
            replayTimes = (cleanSignal.shape[0]
                           // resampledNoiseSignal.shape[0]) + 1
            resampledNoiseSignal = np.repeat(resampledNoiseSignal,
                                             replayTimes)

        # Cutting to the length of the clean signal
        resampledNoiseSignal = resampledNoiseSignal[:cleanSignal.shape[0]]

        # Compute the clean signal power
        cleanSignalPower = np.sum(cleanSignal**2)/cleanSignal.size()

        # Mean shifting the noise data
        noiseSignal = noiseSignal - np.mean(noiseSignal)

        # Creating a noise w.r.t SNR,
        #   Note that SNR here is on decible standard
        pureSNR = 10**(SNR/10)
        targetNoiseVariance = cleanSignalPower / pureSNR
        targetNoiseSignal = (np.sqrt(targetNoiseVariance) * noiseSignal)\
            / np.std(noiseSignal)

        noisyOutput = cleanSignal + targetNoiseSignal

        # If the noisyOutput have values larger than np.int16.max
        # TODO By now we just assumed that this wont happen

        return noisyOutput
