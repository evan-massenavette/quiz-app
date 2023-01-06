<template>
  <v-file-input label="Image" @change="fileChange" @click:clear="clickRemoveImageHandler" :disabled="isSaving"
    :rules="[weight]" accept="image/jpeg, image/png, image/gif" prepend-icon="mdi-camera"></v-file-input>
</template>

<script>
export default {
  emits: ["file-change"],
  data() {
    return {
      isSaving: false,
      fileReader: null,
    };
  },
  props: {},
  mounted() {
    this.fileReader = new FileReader();
    this.fileReader.addEventListener(
      "load",
      () => {
        // fileReader holds a b64 string of the image
        const fileDataUrl = this.fileReader?.result;
        this.isSaving = false;
        this.$emit("file-change", fileDataUrl);
      },
      false
    );
  },
  methods: {
    fileChange(event) {
      this.isSaving = true;
      const input = event.target;
      // pick the first file uploaded
      this.file = input.files[0];
      // feed the file to the asynchronous file reader
      // (next step is in the load eventListener defined in mounted)
      this.fileReader.readAsDataURL(this.file);
    },
    clickRemoveImageHandler() {
      this.$emit("file-change", "");
    },
    weight(value) {
      return !value || !value.length || value[0].size < 2000000 || 'Avatar size should be less than 2 MB!'
    }
  }
};
</script>