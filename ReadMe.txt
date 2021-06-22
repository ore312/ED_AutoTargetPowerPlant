AutoTargetPowerPlant
ore312_作
協力者：
  zura

◆警告◆
  使うのは自己責任でお願いします。
  責任は取りません。

  二次配布は自己責任でお願いします。

▼概要▼
  このツールは設定したキーを押すと設定したサブターゲットに
  自動で合わせてくれるツールです。


▼設定方法▼
  １、EDJPまたはどこかから
       「ED_AutoTargetPowerPlant*.*.*.zip」フォルダと
       「keysee.zip」フォルダをダウンロードします。

  ２、ダウンロードした「ED_AutoTargetPowerPlant*.*.*.zip」フォルダを解凍します。

  ３、解凍したファイル内の「config.json」ファイルをメモ帖で開きます。

  ４、ダウンロードした「keysee.zip」フォルダを解凍します。

  ５、解凍したフォルダ内にある「see.exe」を実行します。

  ６、「see.exe」上でキーを押すと左に文字、真ん中に数字、右に数字が出ます。
       この真ん中に出ている数字をこれからkeycodeと呼びます。
       設定するときに「任意のkeycodeを入力してください。」と出てきたときにこの
       keycodeを使います。

  ７、３で開いた「config.json」の設定をします。
       設定する前にjsonの形式を知らない人は自分で調べよう

▼「config.json」の解説▼
  {
     "Target": [
         {
             "Subsystem": "Power Plant",    ←サブターゲットの名前(ジャーナル内の名前)
             "Key": [
                 39                         ←トリガーになるkeycodeを設定
             ],
             "KeySkip": 7                   ←はじめにスキップするサブシステムの数
         },
         {
             "Subsystem": "Drive",
             "Key": [
                 40
             ],
             "KeySkip": 8
         },
         {
             "Subsystem": "FSD",
             "Key": [
                 43
             ],
             "KeySkip": 6
         }
     ],
     "CYCLE_NEXT_SUBSYSTEM": [              ←エリデン内の「CYCLE NEXT SUBSYSTEM」設定のkeycode
         54,
         82,
         38
     ],
     "CYCLE_PREVIOUS_SUBSYSTEM": [          ←エリデン内の「CYCLE PREVIOUS SUBSYSTEM」設定のkeycode
         54,
         82,
         37
     ],
     "KeyDelay": 0.0125,                    ←キーを仮想的に押すときの長押しする時間(秒)
     "NextRightFlag": true                  ←探索を逆回りから開始するか
  }


▽実際に使ってみる
	1、「AutoTargetPowerPlant.exe」を起動する

	2、エリデン内で設定したキーを押す

	3、自動でターゲットが合う

    ４、殺す

	4、終了方法
		1、黒いウィンドウの右上のバツボタンを押す


エリートでデンジャラスなライフを送ってください。


           _/_/_/_/_/                                      _/
    _/_/          _/        _/_/_/  _/_/_/  _/_/      _/_/_/  _/  _/_/
 _/    _/      _/        _/        _/    _/    _/  _/    _/  _/_/
_/    _/    _/          _/        _/    _/    _/  _/    _/  _/
 _/_/    _/              _/_/_/  _/    _/    _/    _/_/_/  _/
