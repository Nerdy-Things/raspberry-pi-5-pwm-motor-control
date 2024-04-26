import 'dart:convert' as convert;

enum WebsocketCommandType {
  MOTOR,
}

class WebsocketCommand {
  final WebsocketCommandType type;
  final int x;
  final int y;

  const WebsocketCommand({
    required this.type,
    required this.x,
    required this.y,
  });

  String toJson() {
    return convert.jsonEncode({
      'type': type.name.toUpperCase(),
      'x': x,
      'y': y,
    });
  }
}