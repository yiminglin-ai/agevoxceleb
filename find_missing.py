import os
import os.path as osp

downloaded = [osp.splitext(f)[0] for f in os.listdir('data/original_videos')]
# print(downloaded)

with open('./utt2age.test') as f:
    expected = [v.split('/')[1] for v in f]

missing = set([v for v in expected if not v in downloaded])

with open('./data/missing_test.txt', 'w') as f:
    for v in missing: f.write(v+'\n')

with open('./utt2age.train') as f:
    expected = [v.split('/')[1] for v in f]

missing = set([v for v in expected if not v in downloaded])

with open('./data/missing_train.txt', 'w') as f:
    for v in missing: f.write(v+'\n')
