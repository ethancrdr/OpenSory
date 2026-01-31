import { useState, useEffect } from 'react';
import { Shield, CheckCircle, Lock, Download, Play, FileText, Send, ChevronRight, RotateCcw } from 'lucide-react';

function App() {
  // Persistence Logic
  const [currentStep, setCurrentStep] = useState(() => {
    return parseInt(localStorage.getItem('openlock_step') || '1');
  });

  useEffect(() => {
    localStorage.setItem('openlock_step', currentStep);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, [currentStep]);

  const advanceStep = (step) => {
    if (step === currentStep) {
      setCurrentStep(prev => Math.min(prev + 1, 4));
    }
  };

  const resetProgress = () => {
    if (confirm('¿Reiniciar todo el progreso?')) {
      setCurrentStep(1);
      localStorage.removeItem('openlock_step');
    }
  };

  return (
    <div className="app-container">
      {/* Header */}
      {/* Header */}
      <header style={{
        textAlign: 'center',
        marginBottom: '40px',
        background: '#fff',
        padding: '20px',
        borderRadius: '16px',
        boxShadow: '0 4px 20px rgba(0,0,0,0.03)',
        border: '1px solid #f0f0f0',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '20px'
      }}>
        <img src="logo.png" alt="OpenLock" style={{ height: '50px' }} />
        <div style={{ width: '1px', height: '40px', background: '#e0e0e0' }}></div>
        <h2 style={{
          color: 'var(--primary-color)',
          letterSpacing: '1px',
          fontSize: '1.4rem',
          margin: 0,
          fontWeight: 700
        }}>
          OpenLock
        </h2>
      </header>

      {/* Progress Bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '40px', position: 'relative' }}>
        <div style={{
          position: 'absolute', top: '50%', left: 0, right: 0, height: '4px', background: '#ddd', zIndex: 0
        }}></div>
        <div style={{
          position: 'absolute', top: '50%', left: 0, height: '4px', background: 'var(--primary-color)', zIndex: 0,
          width: `${((currentStep - 1) / 3) * 100}%`, transition: 'width 0.5s ease'
        }}></div>

        {[1, 2, 3, 4].map(step => (
          <div key={step} style={{
            width: '40px', height: '40px', borderRadius: '50%',
            background: step <= currentStep ? 'var(--primary-color)' : '#fff',
            border: `3px solid ${step <= currentStep ? 'var(--primary-color)' : '#ddd'}`,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            color: step <= currentStep ? '#fff' : '#666', fontWeight: 'bold', zIndex: 1,
            transition: 'all 0.3s ease'
          }}>
            {step < currentStep ? <CheckCircle size={20} /> : step}
          </div>
        ))}
      </div>

      {/* Steps */}
      <div className="steps-container">

        {/* Step 1 */}
        <MissionCard
          step={1} currentStep={currentStep}
          title="Preparación" subtitle="Descarga de Toolkit" icon={<Download size={32} />}
        >
          <p>Para analizar la seguridad, descargue nuestro paquete de herramientas de solo lectura.</p>
          <div className="instruction-box">
            <ol>
              <li>Descargue <strong>toolkit_opensory_v1.zip</strong>.</li>
              <li>Descomprima en el escritorio.</li>
              <li>Lea la guía PDF incluida.</li>
            </ol>
          </div>
          <div className="actions">
            <a href="toolkit_opensory_v1.zip" download className="btn btn-outline">
              <Download size={18} style={{ marginRight: 8 }} /> Descargar ZIP
            </a>
            <button className="btn btn-primary" onClick={() => advanceStep(1)}>
              Tengo los archivos <ChevronRight size={18} />
            </button>
          </div>
        </MissionCard>

        {/* Step 2 */}
        <MissionCard
          step={2} currentStep={currentStep}
          title="Ejecución" subtitle="Auditoría Automatizada" icon={<Play size={32} />}
        >
          <p>Ejecute los scripts de auditoría en los equipos objetivo.</p>
          <div className="instruction-box">
            <ul>
              <li>Ejecute <code>inventario_activos.py</code></li>
              <li>Ejecute <code>auditoria_politicas.py</code></li>
              <li>Ejecute <code>auditoria_red.py</code></li>
              <li>Ejecute <code>auditoria_av.py</code></li>
            </ul>
          </div>
          <div className="actions">
            <a href="Guia_Uso_OpenSory.pdf" target="_blank" className="btn btn-outline">
              <FileText size={18} style={{ marginRight: 8 }} /> Ver Guía PDF
            </a>
            <button className="btn btn-primary" onClick={() => advanceStep(2)}>
              Scripts Ejecutados <ChevronRight size={18} />
            </button>
          </div>
        </MissionCard>

        {/* Step 3 */}
        <MissionCard
          step={3} currentStep={currentStep}
          title="Cuestionario" subtitle="Políticas Administrativas" icon={<FileText size={32} />}
        >
          <p>Complete el formulario de evaluación de controles administrativos.</p>
          <div style={{ background: '#f8f9fa', padding: '40px', borderRadius: '8px', textAlign: 'center', border: '1px dashed #ccc', margin: '20px 0' }}>
            <h4>[Microsoft Forms Embed Placeholder]</h4>
            <p className="text-muted">Aquí iría el iframe de Forms.</p>
          </div>
          <div className="actions">
            <button className="btn btn-primary" onClick={() => advanceStep(3)}>
              Formulario Enviado <ChevronRight size={18} />
            </button>
          </div>
        </MissionCard>

        {/* Step 4 */}
        <MissionCard
          step={4} currentStep={currentStep}
          title="Entrega" subtitle="Envío de Evidencias" icon={<Send size={32} />}
        >
          <p>Suba los resultados obtenidos a la nube segura.</p>
          <div className="instruction-box">
            <ol>
              <li>Reúna todos los archivos <code>.json</code>.</li>
              <li>Suba todo a OneDrive.</li>
              <li>Notifique al equipo SOC.</li>
            </ol>
          </div>
          <div className="actions">
            <a href="https://onedrive.live.com/" target="_blank" className="btn btn-outline">
              Subir a OneDrive
            </a>
            <a href="mailto:support@opensory.com?subject=Diagnostico%20Finalizado&body=Listo" className="btn btn-primary">
              <Send size={18} style={{ marginRight: 8 }} /> Notificar Finalización
            </a>
          </div>
          <div style={{ marginTop: '40px', textAlign: 'center' }}>
            <button onClick={resetProgress} style={{ background: 'none', border: 'none', color: '#999', textDecoration: 'underline', fontSize: '0.9rem' }}>
              <RotateCcw size={14} style={{ marginRight: 5 }} /> Reiniciar Diagnóstico
            </button>
          </div>
        </MissionCard>

      </div>
    </div>
  );
}

// Sub-component for Cards
function MissionCard({ step, currentStep, title, subtitle, icon, children }) {
  const isLocked = step > currentStep;
  const isCompleted = step < currentStep;

  if (isLocked) {
    return (
      <div style={{
        padding: '40px', borderRadius: '12px', background: '#fff',
        border: '1px solid #eee', marginBottom: '20px',
        opacity: 0.6, filter: 'grayscale(100%)', position: 'relative'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', marginBottom: '20px' }}>
          <div style={{ marginRight: '20px', color: '#ccc' }}><Lock size={32} /></div>
          <div>
            <h2 style={{ margin: 0, fontSize: '1.5rem', color: '#ccc' }}>Misión {step}: Bloqueada</h2>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div style={{
      padding: '40px', borderRadius: '12px', background: '#fff',
      border: '1px solid var(--border-color)', marginBottom: '20px',
      boxShadow: '0 4px 20px rgba(0,0,0,0.05)',
      borderLeft: `5px solid var(--primary-color)`
    }}>
      <div style={{ display: 'flex', alignItems: 'center', marginBottom: '20px' }}>
        <div style={{ marginRight: '20px', color: 'var(--primary-color)' }}>{icon}</div>
        <div>
          <span style={{ textTransform: 'uppercase', letterSpacing: '1px', fontSize: '0.8rem', color: '#888' }}>
            Misión {step}
          </span>
          <h2 style={{ margin: 0, fontSize: '1.5rem' }}>{title}</h2>
          <p style={{ margin: 0, color: 'var(--primary-color)' }}>{subtitle}</p>
        </div>
      </div>
      <div>{children}</div>

      <style>{`
        .instruction-box {
          background: #f0f7fa;
          padding: 20px;
          border-radius: 8px;
          margin: 20px 0;
          border-left: 3px solid var(--primary-color);
        }
        .actions {
          display: flex; gap: 15px; margin-top: 30px; justify-content: flex-end;
          border-top: 1px solid #eee; padding-top: 20px;
        }
        .btn {
          display: inline-flex; align-items: center; justify-content: center;
          padding: 10px 20px; border-radius: 6px; font-weight: 600; text-decoration: none;
          transition: all 0.2s; border: none; font-size: 0.95rem;
        }
        .btn-primary { background: var(--primary-color); color: white; }
        .btn-primary:hover { opacity: 0.9; transform: translateY(-1px); }
        .btn-outline { background: transparent; border: 1px solid var(--primary-color); color: var(--primary-color); }
        .btn-outline:hover { background: rgba(37, 150, 190, 0.05); }
      `}</style>
    </div>
  );
}

export default App;
