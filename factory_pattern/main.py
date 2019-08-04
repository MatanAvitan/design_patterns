from factory_pattern.sender_factory import SenderFactory

if __name__ == '__main__':
    ftp_sender = SenderFactory.get_sender_by_type('FTP')
    ftp_sender.send('here comes a file')
