from cfg import *

def print_language (parser, n, lang_out):
    """Generate n unique random sentences using our grammar and
    print those sentences to lang_out."""

    # Randomly generate n unique sentences
    language = set()
    while True:
        sent = ' '.join(parser.generate('S'))
        language.add(sent)
        print sent
        print len(language) # Uncomment to print

        if len(language) == n:
            break

    # Write the sentences to a file
    f = open(lang_out, 'w')
    '\n'.join(language)

    f.close()

def print_test(parser, test_in, test_out):
    """Given a raw text file, test_in, parse each sentence and write the
    output parse trees to test_out."""

    sentences = open(test_in, 'r')
    f = open(test_out, 'w')
    out = ''
    success_count = 0
    skip_count = 0

    for sent in sentences:
        tokens = sent.split()
        tree = parser.parse(tokens)
        if tree:
            success_count += 1
            out += parser.to_str(tree) + '\n'
            # print 'success {}'.format(success_count) # Uncomment to print
        else:
            skip_count += 1
            out += "({})\n".format(' '.join(["({})".format(t) for t in tokens]))
            # print 'skipped {}'.format(skip_count) # Uncomment to print

    sentences.close()

    f.write(out)
    f.close()

    print 'Parsed sentences = {}'.format(success_count)
    print 'Skipped sentences = {}'.format(skip_count)
    print 'Total sentences = {}'.format(success_count + skip_count)

def main():
    # Create an instance of PCFGParser using the rules in data/weighted.rule
    parser = PCFGParser()
    
    # Run the test
    TEST_IN = 'data/tst.raw'
    TEST_OUT = 'data/tst.parse'
    print_test(parser, TEST_IN, TEST_OUT)

    # Generate a language (random sentences) that are grammatical, but
    # not necessarily meaningful in our grammar !!! DOES NOT WORK !!!
    # SIZE = 100
    # RAND_OUT = 'data/random.raw'
    # print_language(parser, SIZE, RAND_OUT)

if __name__ == '__main__':
    main()
