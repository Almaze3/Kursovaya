<html>
<head>
    <title>Nickname App page</title>
</head>
<body>
    <h2>App nickname</h2>
    <h3>Withdrawn Nickname:</h3>
    <?php
    if (isset($_POST['mail'])){
        $myCurl = curl_init();
    curl_setopt_array($myCurl, array(
        CURLOPT_URL => 'http://nginxserver/api/'.$_POST['mail'],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
    ));
    $response = curl_exec($myCurl);
    $return= curl_exec($myCurl);
    curl_close($myCurl);

    echo "Ответ на Ваш запрос: ".$response;
    }
    ?>
    <form action="index.php" method="post">
    <label for="mail">Origin mail </label>
    <input type="text" name="mail" id="mail" required>
    <input type="submit" value="RUN!">
</body>
</html>