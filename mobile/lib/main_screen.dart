import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter_joystick/flutter_joystick.dart';
import 'package:mobile/websocket_client.dart';
import 'package:mobile/websocket_command.dart';
import 'package:url_launcher/url_launcher.dart';

class MainScreenWidget extends StatelessWidget {
  final _websocketClient = WebSocketClient();

  MainScreenWidget({super.key}) {
    _websocketClient.connect();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black87,
      body: Row(children: [
        Padding(
            padding: const EdgeInsets.all(24.0),
            child: Joystick(listener: (details) {
              var x = min(100, (details.x * 100.0).round());
              x = max(-100, x);
              var y = min(100, (details.y * 100.0).round());
              y = max(-100, y);
              var data = WebsocketCommand(
                type: WebsocketCommandType.MOTOR,
                x: x,
                y: y,
              );
              _websocketClient
                  .send(data)
                  .onError((error, stackTrace) => print(error));
            })),
        Padding(
          padding: const EdgeInsets.all(24.0),
          child: InkWell(
            onTap: () {
              _openYoutube();
            },
            child: Image.asset(
              'assets/images/nerdy_things_channel.png',
              width: 250,
              height: 250,
            ),
          ),
        )
      ]),
    );
  }

  void _openYoutube() async {
    var url = Uri.parse('https://www.youtube.com/@Nerdy.Things');
    if (!await launchUrl(url)) {
      throw Exception('Could not launch $url');
    }
  }
}
