<script setup lang="ts">
type Variant = "primary" | "secondary";

interface Props {
  variant?: Variant;
  type?: "button" | "submit" | "reset";
}

const props = withDefaults(defineProps<Props>(), {
  variant: "primary",
  type: "button",
});

const baseClass =
  "inline-flex items-center justify-center rounded-md px-4 py-2 text-sm font-medium transition focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2";

const variantClass =
  props.variant === "secondary"
    ? "border border-slate-300 bg-white text-slate-900 hover:bg-slate-50 focus-visible:ring-slate-500"
    : "bg-slate-900 text-white hover:bg-slate-700 focus-visible:ring-slate-900";
</script>

<template>
  <button :type="type" :class="[baseClass, variantClass]">
    <slot />
  </button>
</template>
