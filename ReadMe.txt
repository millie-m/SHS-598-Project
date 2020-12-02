To run fluent dataset on deepspeech.

To run test bench on the dataset engine.py in asr-wer-bench can be called using
 python werbench\asr\engine.py --engine deepspeech 
  --model-path-prefix <model dir + model filename prefix>
  --input-dir <wav txt data dir>
  --output-path-prefix <output file prefix>

Please note engine.py input dir needs to contain both wav files and txt files (their correct transcripts).

This will generate ./deepspeech-out.ref and ./deepspeech-out.hyp files.

To generate sclite report:

$ sclite -r deepspeech-out.ref trn -h deepspeech-out.hyp trn -i rm

To generate WER report:
wer deepspeech-out.ref deepspeech-out.hyp

To generate transcrip of a wav file
deepspeech 
  --model models\deepspeech\en-US\deepspeech-0.8.1-models.pbmm 
  --scorer models\deepspeech\en-US\deepspeech-0.8.1-models.scorer 
  --audio path-to-wavfile
