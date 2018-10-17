import os

class NetworkDriveConnectionError(Exception):
    """
    throw out when network drive connection fail
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NetworkDrive(object):
    def __init__(self, remote, user, pw):
        self.remote = remote
        self.user = user
        self.pw = pw

    def __enter__(self):
        # 使用net use連線登入遠端磁碟機
        conn_cmd = 'net use {remote} /user:{username} {pw}'
        conn_cmd = conn_cmd.format(remote=self.remote, username=self.user, pw=self.pw)
        result = os.system(conn_cmd)
        return True if result == 0 else False

    def __exit__(self, type, value, traceback):
        # 使用net use刪除遠端磁碟機連線
        disconn_cmd = 'net use {remote} /delete'
        disconn_cmd = disconn_cmd.format(remote=self.remote)
        os.system(disconn_cmd)
        
def main():

    with NetworkDrive(path, USER, PW) as conn_result:
        if not conn_result:
            raise NetworkDriveConnectionError('Network Drive Connection Fail!')

        # 在遠端目錄目錄找檔案
        onlyfiles = [f for f in os.listdir(path)]
        
if __name__ == '__main__':
    main()
