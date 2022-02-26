# envData

Returns the following output:
`pi@raspberrypi:~ $ sudo python /opt/envData/intTemp1.py
2022-02-26 10:24:06.518994, 56.4485236896315, 45.13160906385901
pi@raspberrypi:~ $ sudo python /opt/envData/extTempOther.py
2022-02-26 10:24:19.498158, 47.71, 61
`

Maybe do something like this for user install:
`ln -s . ~/lib/python3.10/site-packages/`

Assuming you've done a `git clone $URL` to `/opt`, setup crontab:

`*/30 * * * *    sudo /usr/bin/python /opt/envData/extTempOther.py >> ~/eTemp.log
*/30 * * * *    sudo /usr/bin/python /opt/envData/intTemp1.py >> ~/iTemp.log
`
