import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class JsonWriter {

    private static final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    public static void saveSoundMixers(String filePath, List<SoundMixer> data) throws IOException {
        try (FileWriter writer = new FileWriter(filePath)) {
            gson.toJson(data, writer);
        }
    }
}
