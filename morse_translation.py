def text_to_morse(s):
    """
    A code that turns text into visual morse code notation
    -- no punctuation or numerals"""
    if len(s) == 0:
        return ''
    else:
        return letter_to_morse(s[0]) + text_to_morse(s[1:])


def letter_to_morse(lt):
    """ Code that turns letters and spaces into the corresponding morse code
    -- no punctuation or numerals"""
    lt = lt.upper()

    if lt == 'A':
        mc = '.- '
    elif lt == 'B':
        mc = '-... '
    elif lt == 'C':
        mc = '-.-. '
    elif lt == 'D':
        mc = '-.. '
    elif lt == 'E':
        mc = '. '
    elif lt == 'F':
        mc = '..-. '
    elif lt == 'G':
        mc = '--. '
    elif lt == 'H':
        mc = '.... '
    elif lt == 'I':
        mc = '.. '
    elif lt == 'J':
        mc = '.--- '
    elif lt == 'K':
        mc = '-.- '
    elif lt == 'L':
        mc = '.-.. '
    elif lt == 'M':
        mc = '-- '
    elif lt == 'N':
        mc = '-. '
    elif lt == 'O':
        mc = '--- '
    elif lt == 'P':
        mc = '.--. '
    elif lt == 'Q':
        mc = '--.- '
    elif lt == 'R':
        mc = '.-. '
    elif lt == 'S':
        mc = '... '
    elif lt == 'T':
        mc = '- '
    elif lt == 'U':
        mc = '..- '
    elif lt == 'V':
        mc = '...- '
    elif lt == 'W':
        mc = '.-- '
    elif lt == 'X':
        mc = '-..- '
    elif lt == 'Y':
        mc = '-.-- '
    elif lt == 'Z':
        mc = '--.. '
    elif lt == ' ':
        mc = '/'
    else:
        mc = ''
    
    return mc


def morse_to_letter(mc):
    """ Code that turns morse code into the corresponding text and spaces
    -- no punctuation or numerals"""
    if mc == '/':
        lt = ' '
    elif mc == '.-':
        lt = 'A'
    elif mc == '-...':
        lt = 'B'
    elif mc == '-.-.':
        lt = 'C'
    elif mc == '-..':
        lt = 'D'
    elif mc == '.':
        lt = 'E'
    elif mc == '..-.':
        lt = 'F'
    elif mc == '--.':
        lt = 'G'
    elif mc == '....':
        lt = 'H'
    elif mc == '..':
        lt = 'I'
    elif mc == '.---':
        lt = 'J'
    elif mc == '-.-':
        lt = 'K'
    elif mc == '.-..':
        lt = 'L'
    elif mc == '--':
        lt = 'M'
    elif mc == '-.':
        lt = 'N'
    elif mc == '---':
        lt = 'O'
    elif mc == '.--.':
        lt = 'P'
    elif mc == '--.-':
        lt = 'Q'
    elif mc == '.-.':
        lt = 'R'
    elif mc == '...':
        lt = 'S'
    elif mc == '-':
        lt = 'T'
    elif mc == '..-':
        lt = 'U'
    elif mc == '...-':
        lt = 'V'
    elif mc == '.--':
        lt = 'W'
    elif mc == '-..-':
        lt = 'X'
    elif mc == '-.--':
        lt = 'Y'
    elif mc == '--..':
        lt = 'Z'
    else:
        lt = ''
    
    return lt


def morse_to_text(s):
    '''Given a string of morse code, this function translates it into the corresponding text.
    -- does not consider punctuation or numerals'''
    
    if len(s) != 0 and s[-1] != ' ':
        s = s + ' '
        return morse_to_text(s)
    elif len(s) == 0 or (len(s) == 1 and s == ' '):
        return ''
    else:
        spc_el = s.index(' ')
        return morse_to_letter(s[:(spc_el)]) + morse_to_text(s[spc_el+1:])

        

