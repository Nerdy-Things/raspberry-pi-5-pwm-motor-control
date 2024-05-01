import 'package:flutter/material.dart';
import 'package:mobile/websocket_client.dart';
import 'package:mobile/websocket_command.dart';
import 'package:url_launcher/url_launcher.dart';

class SliderScreenWidget extends StatefulWidget {
  const SliderScreenWidget({super.key});

  @override
  State<StatefulWidget> createState() {
    return SliderScreenWidgetState();
  }
}

class SliderScreenWidgetState extends State {
  final _websocketClient = WebSocketClient();
  double _currentSliderValue = 0.0;

  SliderScreenWidgetState() {
    _websocketClient.connect();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black87,
      body: SizedBox(
        width: double.infinity,
        height: double.infinity,
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Padding(
                padding: const EdgeInsets.all(24.0),
                child: Slider(
                  value: _currentSliderValue,
                  min: -100.0,
                  max: 100.0,
                  divisions: 20,
                  activeColor: Colors.purple.shade100,
                  inactiveColor: Colors.purple.shade100,
                  label: _currentSliderValue.round().toString(),
                  onChanged: (double value) {
                    setState(() {
                      _websocketClient.send(WebsocketCommand(
                        type: WebsocketCommandType.MOTOR,
                        x: 0,
                        y: value.toInt(),
                      ));
                      _currentSliderValue = value;
                    });
                  },
                ),
              ),
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
      ),
    );
  }

  void _openYoutube() async {
    var url = Uri.parse('https://www.youtube.com/@Nerdy.Things');
    if (!await launchUrl(url)) {
      throw Exception('Could not launch $url');
    }
  }
}
