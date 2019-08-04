from factory_pattern.api_sender import ApiSender
from factory_pattern.db_sender import DbSender
from factory_pattern.ftp_sender import FtpSender

senders = {
    'API': ApiSender,
    'DB': DbSender,
    'FTP': FtpSender
}


class SenderFactory(object):
    @staticmethod
    def get_sender_by_type(sending_type):
        return senders[sending_type]()
