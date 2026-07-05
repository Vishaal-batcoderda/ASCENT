function GlowBackground() {
  return (
    <div
      className="fixed inset-0 -z-50"
      style={{
        backgroundColor: "#000000",
        backgroundImage: `
          radial-gradient(circle at top left, rgba(59,130,246,0.08), transparent 30%),
          radial-gradient(circle at bottom right, rgba(168,85,247,0.06), transparent 30%)
        `
      }}
    />
  );
}

export default GlowBackground;