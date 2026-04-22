<script setup lang="ts">
import { computed, ref } from "vue";

const count = ref(0);
const label = computed(() => `Clicked ${count.value} time${count.value === 1 ? "" : "s"}`);
</script>

<template>
  <section class="inline-flex items-center gap-3 rounded-lg border border-slate-300 px-4 py-2">
    <button
      type="button"
      class="rounded bg-slate-900 px-3 py-1 text-white hover:bg-slate-700"
      @click="count += 1"
    >
      Increment
    </button>
    <p class="text-sm text-slate-700">{{ label }}</p>
  </section>
</template>
