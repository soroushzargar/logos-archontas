# Used for reading, resampling and writing audio data
import librosa
import librosa.display

# Used for plot functions
import matplotlib.pyplot as plt

# Used for array manipulation
import numpy as np


class representation:
    @staticmethod
    def spectrogram(audioSignal, audioSr, mode="mel"):
        if mode == "mel":
            return librosa.feature.melspectrogram(
                y=audioSignal,
                sr=audioSr
            )
        if mode == "RE":
            return librosa.core.stft(
                y=audioSignal
            )
        return None

    @staticmethod
    def spectrogramFigure(audioSignal=None, audioSr=16000,
                          audioSpectrogram=None, show=True,
                          save=False, saveLocation=None, mode="mel"):
        if audioSignal is not None:
            audioSpectrogram = representation.spectrogram(
                audioSignal, audioSr, mode=mode
            )

        if audioSpectrogram is not None:
            spectroDesible = librosa.power_to_db(
                audioSpectrogram, ref=np.max)
            librosa.display.specshow(spectroDesible, x_axis='time',
                                     y_axis="mel", sr=audioSr,
                                     fmax=8000)
            plt.colorbar(format='%+2.0f dB')
            plt.title('Mel-frequency spectrogram')
            plt.tight_layout()

        if save is True and saveLocation is not None:
            plt.savefig(saveLocation)
        if show is True:
            plt.show()

    def waveFigure(audioSignal=None, audioSr=16000,
                   audioSpectrogram=None, show=True,
                   save=False, saveLocation=None, mode="mel"):
        librosa.display.waveplot(y, sr=sr)
        plt.title('Stereo')
        if save is True and saveLocation is not None:
            plt.savefig(saveLocation)
        if show is True:
            plt.show()