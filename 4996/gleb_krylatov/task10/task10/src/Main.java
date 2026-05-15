void main() {
    System.out.println("Введите адрес");
    Scanner scanner = new Scanner(System.in);
    String ip =  scanner.nextLine();

    System.out.println(checkIP(ip));
}

public String checkIP(String ip) {
    try {
        InetAddress address = InetAddress.getByName(ip);

        // IPv4
        if (ip.contains(".") && address.getHostAddress().equals(ip)) {
            return "IPv4";
        }

        // IPv6
        if (ip.contains(":")) {
            return "IPv6";
        }

    } catch (UnknownHostException e) {
        return "INVALID";
    }

    return "INVALID";
}