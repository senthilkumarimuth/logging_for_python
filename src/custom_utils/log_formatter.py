import logging

FORMAT_STRING = "%(asctime)s | %(process)d | %(name)s | %(funcName)s:%(lineno)d | %(levelname)s | %(message)s"


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super(
            OneLineExceptionFormatter,
            self).formatException(exc_info)
        return repr(result)  # or format into one line however you want to

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '') + ' - log formatted by oneliner'
        return s


FORMATTER = OneLineExceptionFormatter(FORMAT_STRING)
