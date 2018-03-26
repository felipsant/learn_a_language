import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
# UTF8Reader = codecs.getreader('utf8')
# sys.stdin = UTF8Reader(sys.stdin)
