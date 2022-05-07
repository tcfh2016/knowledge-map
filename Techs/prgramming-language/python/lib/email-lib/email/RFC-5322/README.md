## [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322.html)

该RFC定义了互联网邮件信息格式，不过这个RFC仅仅针对的是文本格式的邮件，对于其他如图片、语音等格式是在MIME相关的RFC里面指定的。

+----------------+--------+------------+----------------------------+
| Field          | Min    | Max number | Notes                      |
|                | number |            |                            |
+----------------+--------+------------+----------------------------+
| trace          | 0      | unlimited  | Block prepended - see      |
|                |        |            | 3.6.7                      |
| resent-date    | 0*     | unlimited* | One per block, required if |
|                |        |            | other resent fields are    |
|                |        |            | present - see 3.6.6        |
| resent-from    | 0      | unlimited* | One per block - see 3.6.6  |
| resent-sender  | 0*     | unlimited* | One per block, MUST occur  |
|                |        |            | with multi-address         |
|                |        |            | resent-from - see 3.6.6    |
| resent-to      | 0      | unlimited* | One per block - see 3.6.6  |
| resent-cc      | 0      | unlimited* | One per block - see 3.6.6  |
| resent-bcc     | 0      | unlimited* | One per block - see 3.6.6  |
| resent-msg-id  | 0      | unlimited* | One per block - see 3.6.6  |
| orig-date      | 1      | 1          |                            |
| from           | 1      | 1          | See sender and 3.6.2       |
| sender         | 0*     | 1          | MUST occur with            |
|                |        |            | multi-address from - see   |
|                |        |            | 3.6.2                      |
| reply-to       | 0      | 1          |                            |
| to             | 0      | 1          |                            |
| cc             | 0      | 1          |                            |
| bcc            | 0      | 1          |                            |
| message-id     | 0*     | 1          | SHOULD be present - see    |
|                |        |            | 3.6.4                      |
| in-reply-to    | 0*     | 1          | SHOULD occur in some       |
|                |        |            | replies - see 3.6.4        |
| references     | 0*     | 1          | SHOULD occur in some       |
|                |        |            | replies - see 3.6.4        |
| subject        | 0      | 1          |                            |
| comments       | 0      | unlimited  |                            |
| keywords       | 0      | unlimited  |                            |
| optional-field | 0      | unlimited  |                            |
+----------------+--------+------------+----------------------------+
